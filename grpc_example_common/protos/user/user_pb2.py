# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/user/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="protos/user/user.proto",
    package="user",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x16protos/user/user.proto\x12\x04user\x1a\x1bgoogle/protobuf/empty.proto"E\n\x11\x43reateUserRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t" \n\x11\x44\x65leteUserRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t"1\n\x10LoginUserRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t"@\n\x0fLoginUserResult\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t"/\n\x11LogoutUserRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t""\n\x10\x43heckLoginResult\x12\x0e\n\x06result\x18\x01 \x01(\x08\x32\xc8\x02\n\x04User\x12\x43\n\x10\x63heck_user_login\x12\x17.user.LogoutUserRequest\x1a\x16.user.CheckLoginResult\x12>\n\x0blogout_user\x12\x17.user.LogoutUserRequest\x1a\x16.google.protobuf.Empty\x12;\n\nlogin_user\x12\x16.user.LoginUserRequest\x1a\x15.user.LoginUserResult\x12>\n\x0b\x63reate_user\x12\x17.user.CreateUserRequest\x1a\x16.google.protobuf.Empty\x12>\n\x0b\x64\x65lete_user\x12\x17.user.DeleteUserRequest\x1a\x16.google.protobuf.Emptyb\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
    ],
)


_CREATEUSERREQUEST = _descriptor.Descriptor(
    name="CreateUserRequest",
    full_name="user.CreateUserRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uid",
            full_name="user.CreateUserRequest.uid",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="user_name",
            full_name="user.CreateUserRequest.user_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="password",
            full_name="user.CreateUserRequest.password",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=61,
    serialized_end=130,
)


_DELETEUSERREQUEST = _descriptor.Descriptor(
    name="DeleteUserRequest",
    full_name="user.DeleteUserRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uid",
            full_name="user.DeleteUserRequest.uid",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=132,
    serialized_end=164,
)


_LOGINUSERREQUEST = _descriptor.Descriptor(
    name="LoginUserRequest",
    full_name="user.LoginUserRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uid",
            full_name="user.LoginUserRequest.uid",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="password",
            full_name="user.LoginUserRequest.password",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=166,
    serialized_end=215,
)


_LOGINUSERRESULT = _descriptor.Descriptor(
    name="LoginUserResult",
    full_name="user.LoginUserResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uid",
            full_name="user.LoginUserResult.uid",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="user_name",
            full_name="user.LoginUserResult.user_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="token",
            full_name="user.LoginUserResult.token",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=217,
    serialized_end=281,
)


_LOGOUTUSERREQUEST = _descriptor.Descriptor(
    name="LogoutUserRequest",
    full_name="user.LogoutUserRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uid",
            full_name="user.LogoutUserRequest.uid",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="token",
            full_name="user.LogoutUserRequest.token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=283,
    serialized_end=330,
)


_CHECKLOGINRESULT = _descriptor.Descriptor(
    name="CheckLoginResult",
    full_name="user.CheckLoginResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="result",
            full_name="user.CheckLoginResult.result",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=332,
    serialized_end=366,
)

DESCRIPTOR.message_types_by_name["CreateUserRequest"] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name["DeleteUserRequest"] = _DELETEUSERREQUEST
DESCRIPTOR.message_types_by_name["LoginUserRequest"] = _LOGINUSERREQUEST
DESCRIPTOR.message_types_by_name["LoginUserResult"] = _LOGINUSERRESULT
DESCRIPTOR.message_types_by_name["LogoutUserRequest"] = _LOGOUTUSERREQUEST
DESCRIPTOR.message_types_by_name["CheckLoginResult"] = _CHECKLOGINRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUserRequest = _reflection.GeneratedProtocolMessageType(
    "CreateUserRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEUSERREQUEST,
        "__module__": "protos.user.user_pb2"
        # @@protoc_insertion_point(class_scope:user.CreateUserRequest)
    },
)
_sym_db.RegisterMessage(CreateUserRequest)

DeleteUserRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteUserRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEUSERREQUEST,
        "__module__": "protos.user.user_pb2"
        # @@protoc_insertion_point(class_scope:user.DeleteUserRequest)
    },
)
_sym_db.RegisterMessage(DeleteUserRequest)

LoginUserRequest = _reflection.GeneratedProtocolMessageType(
    "LoginUserRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOGINUSERREQUEST,
        "__module__": "protos.user.user_pb2"
        # @@protoc_insertion_point(class_scope:user.LoginUserRequest)
    },
)
_sym_db.RegisterMessage(LoginUserRequest)

LoginUserResult = _reflection.GeneratedProtocolMessageType(
    "LoginUserResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOGINUSERRESULT,
        "__module__": "protos.user.user_pb2"
        # @@protoc_insertion_point(class_scope:user.LoginUserResult)
    },
)
_sym_db.RegisterMessage(LoginUserResult)

LogoutUserRequest = _reflection.GeneratedProtocolMessageType(
    "LogoutUserRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOGOUTUSERREQUEST,
        "__module__": "protos.user.user_pb2"
        # @@protoc_insertion_point(class_scope:user.LogoutUserRequest)
    },
)
_sym_db.RegisterMessage(LogoutUserRequest)

CheckLoginResult = _reflection.GeneratedProtocolMessageType(
    "CheckLoginResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _CHECKLOGINRESULT,
        "__module__": "protos.user.user_pb2"
        # @@protoc_insertion_point(class_scope:user.CheckLoginResult)
    },
)
_sym_db.RegisterMessage(CheckLoginResult)


_USER = _descriptor.ServiceDescriptor(
    name="User",
    full_name="user.User",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=369,
    serialized_end=697,
    methods=[
        _descriptor.MethodDescriptor(
            name="check_user_login",
            full_name="user.User.check_user_login",
            index=0,
            containing_service=None,
            input_type=_LOGOUTUSERREQUEST,
            output_type=_CHECKLOGINRESULT,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="logout_user",
            full_name="user.User.logout_user",
            index=1,
            containing_service=None,
            input_type=_LOGOUTUSERREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="login_user",
            full_name="user.User.login_user",
            index=2,
            containing_service=None,
            input_type=_LOGINUSERREQUEST,
            output_type=_LOGINUSERRESULT,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="create_user",
            full_name="user.User.create_user",
            index=3,
            containing_service=None,
            input_type=_CREATEUSERREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="delete_user",
            full_name="user.User.delete_user",
            index=4,
            containing_service=None,
            input_type=_DELETEUSERREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name["User"] = _USER

# @@protoc_insertion_point(module_scope)
