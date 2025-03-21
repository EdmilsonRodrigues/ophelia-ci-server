from typing import Annotated

from fastapi import APIRouter, Body, Path, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from ophelia_ci_interface.models.generals import Modal, ModalItem
from ophelia_ci_interface.models.user import (
    CreateUserRequest,
    UpdateUserRequest,
    User,
)
from ophelia_ci_interface.routers.dependencies import (
    Health,
    Metadata,
    Template,
    UserDependency,
)

router = APIRouter(prefix='/users', tags=['User'])


users_modal = Modal(
    title='Create user',
    action='/users/',
    method='POST',
    items=[
        ModalItem(
            id='user_username',
            label='Username',
            type='text',
            autocomplete='username',
        ),
        ModalItem(
            id='user_public_key',
            label='Private Key',
            type='textarea',
            autocomplete='off',
        ),
    ],
    submit='Add user',
    submit_id='user-create',
)

user_modal = Modal(
    title='Update user',
    action='/users/{username}/',
    method='PUT',
    items=[
        ModalItem(
            id='user_username',
            label='User name',
            type='text',
            autocomplete='username',
        ),
        ModalItem(
            id='user_public_key',
            label='Private Key',
            type='textarea',
            autocomplete='off',
        ),
    ],
    submit='Update user',
    submit_id='user-update',
)


@router.get('/', response_class=HTMLResponse)
def users(
    request: Request,
    user_service: UserDependency,
    template: Template,
    health_service: Health,
    metadata: Metadata,
):
    return template.TemplateResponse(
        'users.html',
        {
            'request': request,
            'title': 'Collaborators - Ophelia CI',
            'page_title': 'Collaborators',
            'modal': users_modal,
            'status': health_service.get_status(),
            'repositories': User.get_all(user_service, metadata=metadata),
        },
    )


@router.post('/', response_class=HTMLResponse)
def create_user(
    user_service: UserDependency,
    body: CreateUserRequest,
    template: Template,
    metadata: Metadata,
):
    User.create(
        user_service,
        body.user_username,
        body.user_public_key,
        metadata=metadata,
    )


@router.get('/{username}', response_class=HTMLResponse)
def repository(
    request: Request,
    user_service: UserDependency,
    template: Template,
    health_service: Health,
    metadata: Metadata,
    username: Annotated[
        str, Path(title='Username', description='The username of the user')
    ],
):
    user = User.get_by_username(user_service, username, metadata=metadata)
    return template.TemplateResponse(
        'repository.html',
        {
            'request': request,
            'username': username,
            'status': health_service.get_status(),
            'user': user,
            'id': user.id,
            'modal': user_modal.format_action(username=username),
        },
    )


@router.put('/{username}', status_code=204)
def update_repository(
    user_service: UserDependency,
    body: UpdateUserRequest,
    template: Template,
    metadata: Metadata,
):
    User.update(
        user_service,
        str(body.id),
        body.user_username,
        body.user_public_key,
        metadata=metadata,
    )


@router.delete('/{username}', response_class=RedirectResponse)
def delete_repository(
    request: Request,
    user_service: UserDependency,
    id: Annotated[str, Body(embed=True)],
    template: Template,
    metadata: Metadata,
):
    User.delete(user_service, id, metadata=metadata)
    return RedirectResponse(
        url=request.url_for('repositories'),
        status_code=status.HTTP_303_SEE_OTHER,
    )
