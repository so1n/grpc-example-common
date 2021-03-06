"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CreateBookRequest(google.protobuf.message.Message):
    """create book by admin"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ISBN_FIELD_NUMBER: builtins.int
    BOOK_NAME_FIELD_NUMBER: builtins.int
    BOOK_AUTHOR_FIELD_NUMBER: builtins.int
    BOOK_DESC_FIELD_NUMBER: builtins.int
    BOOK_URL_FIELD_NUMBER: builtins.int
    isbn: typing.Text = ...
    book_name: typing.Text = ...
    book_author: typing.Text = ...
    book_desc: typing.Text = ...
    book_url: typing.Text = ...
    def __init__(self,
        *,
        isbn : typing.Text = ...,
        book_name : typing.Text = ...,
        book_author : typing.Text = ...,
        book_desc : typing.Text = ...,
        book_url : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"book_author",b"book_author",u"book_desc",b"book_desc",u"book_name",b"book_name",u"book_url",b"book_url",u"isbn",b"isbn"]) -> None: ...
global___CreateBookRequest = CreateBookRequest

class DeleteBookRequest(google.protobuf.message.Message):
    """delete book by admin"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ISBN_FIELD_NUMBER: builtins.int
    isbn: typing.Text = ...
    def __init__(self,
        *,
        isbn : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"isbn",b"isbn"]) -> None: ...
global___DeleteBookRequest = DeleteBookRequest

class GetBookRequest(google.protobuf.message.Message):
    """get book by user"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ISBN_FIELD_NUMBER: builtins.int
    isbn: typing.Text = ...
    def __init__(self,
        *,
        isbn : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"isbn",b"isbn"]) -> None: ...
global___GetBookRequest = GetBookRequest

class GetBookResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ISBN_FIELD_NUMBER: builtins.int
    BOOK_NAME_FIELD_NUMBER: builtins.int
    BOOK_AUTHOR_FIELD_NUMBER: builtins.int
    BOOK_DESC_FIELD_NUMBER: builtins.int
    BOOK_URL_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    isbn: typing.Text = ...
    book_name: typing.Text = ...
    book_author: typing.Text = ...
    book_desc: typing.Text = ...
    book_url: typing.Text = ...
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        isbn : typing.Text = ...,
        book_name : typing.Text = ...,
        book_author : typing.Text = ...,
        book_desc : typing.Text = ...,
        book_url : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"create_time",b"create_time",u"update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"book_author",b"book_author",u"book_desc",b"book_desc",u"book_name",b"book_name",u"book_url",b"book_url",u"create_time",b"create_time",u"isbn",b"isbn",u"update_time",b"update_time"]) -> None: ...
global___GetBookResult = GetBookResult

class GetBookListRequest(google.protobuf.message.Message):
    """get book list by user"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NEXT_CREATE_TIME_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    @property
    def next_create_time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    limit: builtins.int = ...
    def __init__(self,
        *,
        next_create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        limit : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"_next_create_time",b"_next_create_time",u"next_create_time",b"next_create_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"_next_create_time",b"_next_create_time",u"limit",b"limit",u"next_create_time",b"next_create_time"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_next_create_time",b"_next_create_time"]) -> typing.Optional[typing_extensions.Literal["next_create_time"]]: ...
global___GetBookListRequest = GetBookListRequest

class GetBookListResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GetBookResult]: ...
    def __init__(self,
        *,
        result : typing.Optional[typing.Iterable[global___GetBookResult]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"result",b"result"]) -> None: ...
global___GetBookListResult = GetBookListResult
