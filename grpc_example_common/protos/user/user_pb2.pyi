"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CreateUserRequest(google.protobuf.message.Message):
    """create user"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    uid: typing.Text = ...
    user_name: typing.Text = ...
    password: typing.Text = ...
    def __init__(self,
        *,
        uid : typing.Text = ...,
        user_name : typing.Text = ...,
        password : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"password",b"password",u"uid",b"uid",u"user_name",b"user_name"]) -> None: ...
global___CreateUserRequest = CreateUserRequest

class DeleteUserRequest(google.protobuf.message.Message):
    """delete user"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UID_FIELD_NUMBER: builtins.int
    uid: typing.Text = ...
    def __init__(self,
        *,
        uid : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"uid",b"uid"]) -> None: ...
global___DeleteUserRequest = DeleteUserRequest

class LoginUserRequest(google.protobuf.message.Message):
    """login user"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UID_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    uid: typing.Text = ...
    password: typing.Text = ...
    def __init__(self,
        *,
        uid : typing.Text = ...,
        password : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"password",b"password",u"uid",b"uid"]) -> None: ...
global___LoginUserRequest = LoginUserRequest

class LoginUserResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    TOKEN_FIELD_NUMBER: builtins.int
    uid: typing.Text = ...
    user_name: typing.Text = ...
    token: typing.Text = ...
    def __init__(self,
        *,
        uid : typing.Text = ...,
        user_name : typing.Text = ...,
        token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"token",b"token",u"uid",b"uid",u"user_name",b"user_name"]) -> None: ...
global___LoginUserResult = LoginUserResult

class LogoutUserRequest(google.protobuf.message.Message):
    """logout user"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UID_FIELD_NUMBER: builtins.int
    TOKEN_FIELD_NUMBER: builtins.int
    uid: typing.Text = ...
    token: typing.Text = ...
    def __init__(self,
        *,
        uid : typing.Text = ...,
        token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"token",b"token",u"uid",b"uid"]) -> None: ...
global___LogoutUserRequest = LogoutUserRequest

class GetUidByTokenRequest(google.protobuf.message.Message):
    """check login"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOKEN_FIELD_NUMBER: builtins.int
    token: typing.Text = ...
    def __init__(self,
        *,
        token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"token",b"token"]) -> None: ...
global___GetUidByTokenRequest = GetUidByTokenRequest

class GetUidByTokenResult(google.protobuf.message.Message):
    """check login"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UID_FIELD_NUMBER: builtins.int
    uid: typing.Text = ...
    def __init__(self,
        *,
        uid : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"uid",b"uid"]) -> None: ...
global___GetUidByTokenResult = GetUidByTokenResult
