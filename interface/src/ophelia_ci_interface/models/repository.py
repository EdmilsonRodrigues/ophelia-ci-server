from datetime import datetime
from functools import cache

from google.protobuf.timestamp_pb2 import Timestamp
from ophelia_ci_interface.config import Settings
from ophelia_ci_interface.services.gRPC_service import RepositoryService
from pydantic import UUID4, BaseModel, model_validator


class CreateRepositoryRequest(BaseModel):
    repository_name: str
    repository_description: str
    repository_gitignore: str


class UpdateRepositoryRequest(BaseModel):
    id: UUID4
    repository_name: str
    repository_description: str


class Repository(BaseModel):
    model_config = {'arbitrary_types_allowed': True}

    id: UUID4
    name: str
    description: str
    last_updated: datetime

    @model_validator(mode='before')
    def parse_timestamp(cls, value):
        value['last_updated'] = cls.convert_timestamp_to_datetime(
            value['last_updated']
        )
        return value

    @staticmethod
    @cache
    def get_service() -> RepositoryService:
        return RepositoryService(str(Settings().GRPC_SERVER))

    @property
    def truncated_description(self):
        if len(self.description) > 100:
            return self.description[:100] + '...'
        return self.description

    @property
    def clone_url(self):
        return f'git@{str(Settings().GRPC_SERVER).rstrip("/")}:{self.name}.git'

    @classmethod
    def get_status(cls):
        return cls.get_service().get_status()

    @staticmethod
    def convert_timestamp_to_datetime(timestamp: Timestamp) -> datetime:
        return timestamp.ToDatetime()

    @classmethod
    def create(cls, name: str, description: str, gitignore: str):
        response = cls.get_service().create_repository(
            name, description, gitignore
        )
        return cls(
            id=response.id,
            name=response.name,
            description=response.description,
            last_updated=response.last_update,
        )

    @classmethod
    def update(cls, id: str, name: str, description: str):
        response = cls.get_service().update_repository(id, name, description)
        return cls(
            id=response.id,
            name=response.name,
            description=response.description,
            last_updated=response.last_update,
        )

    @classmethod
    def get(cls, id: str):
        response = cls.get_service().get_repository(id)
        return cls(
            id=response.id,
            name=response.name,
            description=response.description,
            last_updated=response.last_update,
        )

    @classmethod
    def get_by_name(cls, name: str):
        response = cls.get_service().get_by_name(name)
        return cls(
            id=response.id,
            name=response.name,
            description=response.description,
            last_updated=response.last_update,
        )

    @classmethod
    def delete(cls, id: str):
        cls.get_service().delete_repository(id)

    @classmethod
    def get_all(cls):
        response_list = cls.get_service().get_repositories()
        return [
            cls(
                id=response.id,
                name=response.name,
                description=response.description,
                last_updated=response.last_update,
            )
            for response in response_list.repositories
        ]
