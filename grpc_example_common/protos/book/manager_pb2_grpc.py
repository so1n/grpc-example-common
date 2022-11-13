# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from grpc_example_common.protos.book import manager_pb2 as grpc__example__common_dot_protos_dot_book_dot_manager__pb2


class BookManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create_book = channel.unary_unary(
                '/book_manager.BookManager/create_book',
                request_serializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.CreateBookRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.delete_book = channel.unary_unary(
                '/book_manager.BookManager/delete_book',
                request_serializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.DeleteBookRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get_book = channel.unary_unary(
                '/book_manager.BookManager/get_book',
                request_serializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookRequest.SerializeToString,
                response_deserializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookResult.FromString,
                )
        self.get_book_list = channel.unary_unary(
                '/book_manager.BookManager/get_book_list',
                request_serializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookListRequest.SerializeToString,
                response_deserializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookListResult.FromString,
                )


class BookManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create_book(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_book(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_book(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_book_list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create_book': grpc.unary_unary_rpc_method_handler(
                    servicer.create_book,
                    request_deserializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.CreateBookRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'delete_book': grpc.unary_unary_rpc_method_handler(
                    servicer.delete_book,
                    request_deserializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.DeleteBookRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get_book': grpc.unary_unary_rpc_method_handler(
                    servicer.get_book,
                    request_deserializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookRequest.FromString,
                    response_serializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookResult.SerializeToString,
            ),
            'get_book_list': grpc.unary_unary_rpc_method_handler(
                    servicer.get_book_list,
                    request_deserializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookListRequest.FromString,
                    response_serializer=grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookListResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'book_manager.BookManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create_book(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book_manager.BookManager/create_book',
            grpc__example__common_dot_protos_dot_book_dot_manager__pb2.CreateBookRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete_book(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book_manager.BookManager/delete_book',
            grpc__example__common_dot_protos_dot_book_dot_manager__pb2.DeleteBookRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_book(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book_manager.BookManager/get_book',
            grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookRequest.SerializeToString,
            grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_book_list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book_manager.BookManager/get_book_list',
            grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookListRequest.SerializeToString,
            grpc__example__common_dot_protos_dot_book_dot_manager__pb2.GetBookListResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
