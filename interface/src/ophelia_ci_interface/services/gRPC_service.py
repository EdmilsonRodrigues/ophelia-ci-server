import grpc
import ophelia_ci_interface.services.repository_pb2 as repository_pb2
import ophelia_ci_interface.services.repository_pb2_grpc as repository_pb2_grpc


class RepositoryService:
    def __init__(self, server: str):
        self.server = server
        self.channel = None
        self.stub = None

    def __enter__(self):
        self.channel = grpc.insecure_channel(self.server)
        self.stub = repository_pb2_grpc.RepositoryServiceStub(self.channel)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.channel.close()

    def get_status(self):
        return 'Connected'

    def get_repositories(self):
        with self:
            response_list = self.stub.ListRepository(repository_pb2.Empty())
        return response_list

    def create_repository(self, name: str, description: str, gitignore: str):
        with self:
            response_create = self.stub.CreateRepository(
                repository_pb2.CreateRepositoryRequest(
                    name=name, description=description, gitignore=gitignore
                )
            )
        return response_create

    def update_repository(self, id: str, name: str, description: str):
        with self:
            response_update = self.stub.UpdateRepository(
                repository_pb2.UpdateRepositoryRequest(
                    id=id, name=name, description=description
                )
            )
        return response_update

    def get_repository(self, id: str):
        with self:
            response_get = self.stub.GetRepository(
                repository_pb2.GetRepositoryRequest(id=id)
            )
        return response_get

    def get_by_name(self, name: str):
        with self:
            response_get = self.stub.GetRepositoryByName(
                repository_pb2.GetRepositoryByNameRequest(name=name)
            )
        return response_get

    def delete_repository(self, id: str):
        with self:
            response_delete = self.stub.DeleteRepository(
                repository_pb2.DeleteRepositoryRequest(id=id)
            )
        return response_delete
