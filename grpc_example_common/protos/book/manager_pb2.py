# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/book/manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/book/manager.proto',
  package='book_manager',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19protos/book/manager.proto\x12\x0c\x62ook_manager\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"n\n\x11\x43reateBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x11\n\tbook_name\x18\x02 \x01(\t\x12\x13\n\x0b\x62ook_author\x18\x03 \x01(\t\x12\x11\n\tbook_desc\x18\x04 \x01(\t\x12\x10\n\x08\x62ook_url\x18\x05 \x01(\t\"!\n\x11\x44\x65leteBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"\xcc\x01\n\rGetBookResult\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x11\n\tbook_name\x18\x02 \x01(\t\x12\x13\n\x0b\x62ook_author\x18\x03 \x01(\t\x12\x11\n\tbook_desc\x18\x04 \x01(\t\x12\x10\n\x08\x62ook_url\x18\x05 \x01(\t\x12/\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"s\n\x12GetBookListRequest\x12\x39\n\x10next_create_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12\r\n\x05limit\x18\x02 \x01(\x05\x42\x13\n\x11_next_create_time\"@\n\x11GetBookListResult\x12+\n\x06result\x18\x01 \x03(\x0b\x32\x1b.book_manager.GetBookResult2\xb8\x02\n\x0b\x42ookManager\x12\x46\n\x0b\x63reate_book\x12\x1f.book_manager.CreateBookRequest\x1a\x16.google.protobuf.Empty\x12\x46\n\x0b\x64\x65lete_book\x12\x1f.book_manager.DeleteBookRequest\x1a\x16.google.protobuf.Empty\x12\x45\n\x08get_book\x12\x1c.book_manager.GetBookRequest\x1a\x1b.book_manager.GetBookResult\x12R\n\rget_book_list\x12 .book_manager.GetBookListRequest\x1a\x1f.book_manager.GetBookListResultb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CREATEBOOKREQUEST = _descriptor.Descriptor(
  name='CreateBookRequest',
  full_name='book_manager.CreateBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='book_manager.CreateBookRequest.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_name', full_name='book_manager.CreateBookRequest.book_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_author', full_name='book_manager.CreateBookRequest.book_author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_desc', full_name='book_manager.CreateBookRequest.book_desc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_url', full_name='book_manager.CreateBookRequest.book_url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=215,
)


_DELETEBOOKREQUEST = _descriptor.Descriptor(
  name='DeleteBookRequest',
  full_name='book_manager.DeleteBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='book_manager.DeleteBookRequest.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=250,
)


_GETBOOKREQUEST = _descriptor.Descriptor(
  name='GetBookRequest',
  full_name='book_manager.GetBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='book_manager.GetBookRequest.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=282,
)


_GETBOOKRESULT = _descriptor.Descriptor(
  name='GetBookResult',
  full_name='book_manager.GetBookResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='book_manager.GetBookResult.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_name', full_name='book_manager.GetBookResult.book_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_author', full_name='book_manager.GetBookResult.book_author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_desc', full_name='book_manager.GetBookResult.book_desc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_url', full_name='book_manager.GetBookResult.book_url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='book_manager.GetBookResult.create_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='book_manager.GetBookResult.update_time', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=489,
)


_GETBOOKLISTREQUEST = _descriptor.Descriptor(
  name='GetBookListRequest',
  full_name='book_manager.GetBookListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_create_time', full_name='book_manager.GetBookListRequest.next_create_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='book_manager.GetBookListRequest.limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_next_create_time', full_name='book_manager.GetBookListRequest._next_create_time',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=491,
  serialized_end=606,
)


_GETBOOKLISTRESULT = _descriptor.Descriptor(
  name='GetBookListResult',
  full_name='book_manager.GetBookListResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='book_manager.GetBookListResult.result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=608,
  serialized_end=672,
)

_GETBOOKRESULT.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETBOOKRESULT.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETBOOKLISTREQUEST.fields_by_name['next_create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETBOOKLISTREQUEST.oneofs_by_name['_next_create_time'].fields.append(
  _GETBOOKLISTREQUEST.fields_by_name['next_create_time'])
_GETBOOKLISTREQUEST.fields_by_name['next_create_time'].containing_oneof = _GETBOOKLISTREQUEST.oneofs_by_name['_next_create_time']
_GETBOOKLISTRESULT.fields_by_name['result'].message_type = _GETBOOKRESULT
DESCRIPTOR.message_types_by_name['CreateBookRequest'] = _CREATEBOOKREQUEST
DESCRIPTOR.message_types_by_name['DeleteBookRequest'] = _DELETEBOOKREQUEST
DESCRIPTOR.message_types_by_name['GetBookRequest'] = _GETBOOKREQUEST
DESCRIPTOR.message_types_by_name['GetBookResult'] = _GETBOOKRESULT
DESCRIPTOR.message_types_by_name['GetBookListRequest'] = _GETBOOKLISTREQUEST
DESCRIPTOR.message_types_by_name['GetBookListResult'] = _GETBOOKLISTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateBookRequest = _reflection.GeneratedProtocolMessageType('CreateBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBOOKREQUEST,
  '__module__' : 'protos.book.manager_pb2'
  # @@protoc_insertion_point(class_scope:book_manager.CreateBookRequest)
  })
_sym_db.RegisterMessage(CreateBookRequest)

DeleteBookRequest = _reflection.GeneratedProtocolMessageType('DeleteBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBOOKREQUEST,
  '__module__' : 'protos.book.manager_pb2'
  # @@protoc_insertion_point(class_scope:book_manager.DeleteBookRequest)
  })
_sym_db.RegisterMessage(DeleteBookRequest)

GetBookRequest = _reflection.GeneratedProtocolMessageType('GetBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKREQUEST,
  '__module__' : 'protos.book.manager_pb2'
  # @@protoc_insertion_point(class_scope:book_manager.GetBookRequest)
  })
_sym_db.RegisterMessage(GetBookRequest)

GetBookResult = _reflection.GeneratedProtocolMessageType('GetBookResult', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKRESULT,
  '__module__' : 'protos.book.manager_pb2'
  # @@protoc_insertion_point(class_scope:book_manager.GetBookResult)
  })
_sym_db.RegisterMessage(GetBookResult)

GetBookListRequest = _reflection.GeneratedProtocolMessageType('GetBookListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKLISTREQUEST,
  '__module__' : 'protos.book.manager_pb2'
  # @@protoc_insertion_point(class_scope:book_manager.GetBookListRequest)
  })
_sym_db.RegisterMessage(GetBookListRequest)

GetBookListResult = _reflection.GeneratedProtocolMessageType('GetBookListResult', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKLISTRESULT,
  '__module__' : 'protos.book.manager_pb2'
  # @@protoc_insertion_point(class_scope:book_manager.GetBookListResult)
  })
_sym_db.RegisterMessage(GetBookListResult)



_BOOKMANAGER = _descriptor.ServiceDescriptor(
  name='BookManager',
  full_name='book_manager.BookManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=675,
  serialized_end=987,
  methods=[
  _descriptor.MethodDescriptor(
    name='create_book',
    full_name='book_manager.BookManager.create_book',
    index=0,
    containing_service=None,
    input_type=_CREATEBOOKREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete_book',
    full_name='book_manager.BookManager.delete_book',
    index=1,
    containing_service=None,
    input_type=_DELETEBOOKREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_book',
    full_name='book_manager.BookManager.get_book',
    index=2,
    containing_service=None,
    input_type=_GETBOOKREQUEST,
    output_type=_GETBOOKRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_book_list',
    full_name='book_manager.BookManager.get_book_list',
    index=3,
    containing_service=None,
    input_type=_GETBOOKLISTREQUEST,
    output_type=_GETBOOKLISTRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKMANAGER)

DESCRIPTOR.services_by_name['BookManager'] = _BOOKMANAGER

# @@protoc_insertion_point(module_scope)
