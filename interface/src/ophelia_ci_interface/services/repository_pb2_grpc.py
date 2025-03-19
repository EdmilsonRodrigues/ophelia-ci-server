# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import ophelia_ci_interface.services.repository_pb2 as repository__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in repository_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class RepositoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateRepository = channel.unary_unary(
                '/ophelia.RepositoryService/CreateRepository',
                request_serializer=repository__pb2.CreateRepositoryRequest.SerializeToString,
                response_deserializer=repository__pb2.RepositoryResponse.FromString,
                _registered_method=True)
        self.UpdateRepository = channel.unary_unary(
                '/ophelia.RepositoryService/UpdateRepository',
                request_serializer=repository__pb2.UpdateRepositoryRequest.SerializeToString,
                response_deserializer=repository__pb2.RepositoryResponse.FromString,
                _registered_method=True)
        self.ListRepository = channel.unary_unary(
                '/ophelia.RepositoryService/ListRepository',
                request_serializer=repository__pb2.Empty.SerializeToString,
                response_deserializer=repository__pb2.ListRepositoryResponse.FromString,
                _registered_method=True)
        self.GetRepository = channel.unary_unary(
                '/ophelia.RepositoryService/GetRepository',
                request_serializer=repository__pb2.GetRepositoryRequest.SerializeToString,
                response_deserializer=repository__pb2.RepositoryResponse.FromString,
                _registered_method=True)
        self.DeleteRepository = channel.unary_unary(
                '/ophelia.RepositoryService/DeleteRepository',
                request_serializer=repository__pb2.DeleteRepositoryRequest.SerializeToString,
                response_deserializer=repository__pb2.Empty.FromString,
                _registered_method=True)


class RepositoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateRepository(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRepository(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRepository(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRepository(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRepository(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RepositoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateRepository': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRepository,
                    request_deserializer=repository__pb2.CreateRepositoryRequest.FromString,
                    response_serializer=repository__pb2.RepositoryResponse.SerializeToString,
            ),
            'UpdateRepository': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRepository,
                    request_deserializer=repository__pb2.UpdateRepositoryRequest.FromString,
                    response_serializer=repository__pb2.RepositoryResponse.SerializeToString,
            ),
            'ListRepository': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRepository,
                    request_deserializer=repository__pb2.Empty.FromString,
                    response_serializer=repository__pb2.ListRepositoryResponse.SerializeToString,
            ),
            'GetRepository': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRepository,
                    request_deserializer=repository__pb2.GetRepositoryRequest.FromString,
                    response_serializer=repository__pb2.RepositoryResponse.SerializeToString,
            ),
            'DeleteRepository': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRepository,
                    request_deserializer=repository__pb2.DeleteRepositoryRequest.FromString,
                    response_serializer=repository__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ophelia.RepositoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ophelia.RepositoryService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RepositoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateRepository(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ophelia.RepositoryService/CreateRepository',
            repository__pb2.CreateRepositoryRequest.SerializeToString,
            repository__pb2.RepositoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateRepository(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ophelia.RepositoryService/UpdateRepository',
            repository__pb2.UpdateRepositoryRequest.SerializeToString,
            repository__pb2.RepositoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListRepository(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ophelia.RepositoryService/ListRepository',
            repository__pb2.Empty.SerializeToString,
            repository__pb2.ListRepositoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRepository(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ophelia.RepositoryService/GetRepository',
            repository__pb2.GetRepositoryRequest.SerializeToString,
            repository__pb2.RepositoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteRepository(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ophelia.RepositoryService/DeleteRepository',
            repository__pb2.DeleteRepositoryRequest.SerializeToString,
            repository__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
