# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/book/social.proto
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
  name='protos/book/social.proto',
  package='book_social',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18protos/book/social.proto\x12\x0b\x62ook_social\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\":\n\x0fLikeBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x0c\n\x04like\x18\x02 \x01(\x08\x12\x0b\n\x03uid\x18\x03 \x01(\t\"#\n\x13GetBookLikesRequest\x12\x0c\n\x04isbn\x18\x01 \x03(\t\"5\n\x12GetBookLikesResult\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x11\n\tbook_like\x18\x02 \x01(\x05\"I\n\x16GetBookLikesListResult\x12/\n\x06result\x18\x01 \x03(\x0b\x32\x1f.book_social.GetBookLikesResult\"@\n\x12\x43ommentBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\t\"\x93\x01\n\x15GetBookCommentRequest\x12\x0c\n\x04isbn\x18\x01 \x03(\t\x12\x39\n\x10next_create_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12\x12\n\x05limit\x18\x03 \x01(\x05H\x01\x88\x01\x01\x42\x13\n\x11_next_create_timeB\x08\n\x06_limit\"s\n\x14GetBookCommentResult\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\t\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"M\n\x18GetBookCommentListResult\x12\x31\n\x06result\x18\x01 \x03(\x0b\x32!.book_social.GetBookCommentResult2\xcf\x02\n\nBookSocial\x12\x41\n\tlike_book\x12\x1c.book_social.LikeBookRequest\x1a\x16.google.protobuf.Empty\x12V\n\rget_book_like\x12 .book_social.GetBookLikesRequest\x1a#.book_social.GetBookLikesListResult\x12G\n\x0c\x63omment_book\x12\x1f.book_social.CommentBookRequest\x1a\x16.google.protobuf.Empty\x12]\n\x10get_book_comment\x12\".book_social.GetBookCommentRequest\x1a%.book_social.GetBookCommentListResultb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_LIKEBOOKREQUEST = _descriptor.Descriptor(
  name='LikeBookRequest',
  full_name='book_social.LikeBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='book_social.LikeBookRequest.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='like', full_name='book_social.LikeBookRequest.like', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uid', full_name='book_social.LikeBookRequest.uid', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=103,
  serialized_end=161,
)


_GETBOOKLIKESREQUEST = _descriptor.Descriptor(
  name='GetBookLikesRequest',
  full_name='book_social.GetBookLikesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='book_social.GetBookLikesRequest.isbn', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=163,
  serialized_end=198,
)


_GETBOOKLIKESRESULT = _descriptor.Descriptor(
  name='GetBookLikesResult',
  full_name='book_social.GetBookLikesResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='book_social.GetBookLikesResult.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_like', full_name='book_social.GetBookLikesResult.book_like', index=1,
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
  ],
  serialized_start=200,
  serialized_end=253,
)


_GETBOOKLIKESLISTRESULT = _descriptor.Descriptor(
  name='GetBookLikesListResult',
  full_name='book_social.GetBookLikesListResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='book_social.GetBookLikesListResult.result', index=0,
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
  serialized_start=255,
  serialized_end=328,
)


_COMMENTBOOKREQUEST = _descriptor.Descriptor(
  name='CommentBookRequest',
  full_name='book_social.CommentBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='book_social.CommentBookRequest.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='book_social.CommentBookRequest.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uid', full_name='book_social.CommentBookRequest.uid', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=330,
  serialized_end=394,
)


_GETBOOKCOMMENTREQUEST = _descriptor.Descriptor(
  name='GetBookCommentRequest',
  full_name='book_social.GetBookCommentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='book_social.GetBookCommentRequest.isbn', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_create_time', full_name='book_social.GetBookCommentRequest.next_create_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='book_social.GetBookCommentRequest.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
      name='_next_create_time', full_name='book_social.GetBookCommentRequest._next_create_time',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_limit', full_name='book_social.GetBookCommentRequest._limit',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=397,
  serialized_end=544,
)


_GETBOOKCOMMENTRESULT = _descriptor.Descriptor(
  name='GetBookCommentResult',
  full_name='book_social.GetBookCommentResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='book_social.GetBookCommentResult.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='book_social.GetBookCommentResult.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uid', full_name='book_social.GetBookCommentResult.uid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='book_social.GetBookCommentResult.create_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=546,
  serialized_end=661,
)


_GETBOOKCOMMENTLISTRESULT = _descriptor.Descriptor(
  name='GetBookCommentListResult',
  full_name='book_social.GetBookCommentListResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='book_social.GetBookCommentListResult.result', index=0,
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
  serialized_start=663,
  serialized_end=740,
)

_GETBOOKLIKESLISTRESULT.fields_by_name['result'].message_type = _GETBOOKLIKESRESULT
_GETBOOKCOMMENTREQUEST.fields_by_name['next_create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETBOOKCOMMENTREQUEST.oneofs_by_name['_next_create_time'].fields.append(
  _GETBOOKCOMMENTREQUEST.fields_by_name['next_create_time'])
_GETBOOKCOMMENTREQUEST.fields_by_name['next_create_time'].containing_oneof = _GETBOOKCOMMENTREQUEST.oneofs_by_name['_next_create_time']
_GETBOOKCOMMENTREQUEST.oneofs_by_name['_limit'].fields.append(
  _GETBOOKCOMMENTREQUEST.fields_by_name['limit'])
_GETBOOKCOMMENTREQUEST.fields_by_name['limit'].containing_oneof = _GETBOOKCOMMENTREQUEST.oneofs_by_name['_limit']
_GETBOOKCOMMENTRESULT.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETBOOKCOMMENTLISTRESULT.fields_by_name['result'].message_type = _GETBOOKCOMMENTRESULT
DESCRIPTOR.message_types_by_name['LikeBookRequest'] = _LIKEBOOKREQUEST
DESCRIPTOR.message_types_by_name['GetBookLikesRequest'] = _GETBOOKLIKESREQUEST
DESCRIPTOR.message_types_by_name['GetBookLikesResult'] = _GETBOOKLIKESRESULT
DESCRIPTOR.message_types_by_name['GetBookLikesListResult'] = _GETBOOKLIKESLISTRESULT
DESCRIPTOR.message_types_by_name['CommentBookRequest'] = _COMMENTBOOKREQUEST
DESCRIPTOR.message_types_by_name['GetBookCommentRequest'] = _GETBOOKCOMMENTREQUEST
DESCRIPTOR.message_types_by_name['GetBookCommentResult'] = _GETBOOKCOMMENTRESULT
DESCRIPTOR.message_types_by_name['GetBookCommentListResult'] = _GETBOOKCOMMENTLISTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LikeBookRequest = _reflection.GeneratedProtocolMessageType('LikeBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _LIKEBOOKREQUEST,
  '__module__' : 'protos.book.social_pb2'
  # @@protoc_insertion_point(class_scope:book_social.LikeBookRequest)
  })
_sym_db.RegisterMessage(LikeBookRequest)

GetBookLikesRequest = _reflection.GeneratedProtocolMessageType('GetBookLikesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKLIKESREQUEST,
  '__module__' : 'protos.book.social_pb2'
  # @@protoc_insertion_point(class_scope:book_social.GetBookLikesRequest)
  })
_sym_db.RegisterMessage(GetBookLikesRequest)

GetBookLikesResult = _reflection.GeneratedProtocolMessageType('GetBookLikesResult', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKLIKESRESULT,
  '__module__' : 'protos.book.social_pb2'
  # @@protoc_insertion_point(class_scope:book_social.GetBookLikesResult)
  })
_sym_db.RegisterMessage(GetBookLikesResult)

GetBookLikesListResult = _reflection.GeneratedProtocolMessageType('GetBookLikesListResult', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKLIKESLISTRESULT,
  '__module__' : 'protos.book.social_pb2'
  # @@protoc_insertion_point(class_scope:book_social.GetBookLikesListResult)
  })
_sym_db.RegisterMessage(GetBookLikesListResult)

CommentBookRequest = _reflection.GeneratedProtocolMessageType('CommentBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMENTBOOKREQUEST,
  '__module__' : 'protos.book.social_pb2'
  # @@protoc_insertion_point(class_scope:book_social.CommentBookRequest)
  })
_sym_db.RegisterMessage(CommentBookRequest)

GetBookCommentRequest = _reflection.GeneratedProtocolMessageType('GetBookCommentRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKCOMMENTREQUEST,
  '__module__' : 'protos.book.social_pb2'
  # @@protoc_insertion_point(class_scope:book_social.GetBookCommentRequest)
  })
_sym_db.RegisterMessage(GetBookCommentRequest)

GetBookCommentResult = _reflection.GeneratedProtocolMessageType('GetBookCommentResult', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKCOMMENTRESULT,
  '__module__' : 'protos.book.social_pb2'
  # @@protoc_insertion_point(class_scope:book_social.GetBookCommentResult)
  })
_sym_db.RegisterMessage(GetBookCommentResult)

GetBookCommentListResult = _reflection.GeneratedProtocolMessageType('GetBookCommentListResult', (_message.Message,), {
  'DESCRIPTOR' : _GETBOOKCOMMENTLISTRESULT,
  '__module__' : 'protos.book.social_pb2'
  # @@protoc_insertion_point(class_scope:book_social.GetBookCommentListResult)
  })
_sym_db.RegisterMessage(GetBookCommentListResult)



_BOOKSOCIAL = _descriptor.ServiceDescriptor(
  name='BookSocial',
  full_name='book_social.BookSocial',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=743,
  serialized_end=1078,
  methods=[
  _descriptor.MethodDescriptor(
    name='like_book',
    full_name='book_social.BookSocial.like_book',
    index=0,
    containing_service=None,
    input_type=_LIKEBOOKREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_book_like',
    full_name='book_social.BookSocial.get_book_like',
    index=1,
    containing_service=None,
    input_type=_GETBOOKLIKESREQUEST,
    output_type=_GETBOOKLIKESLISTRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='comment_book',
    full_name='book_social.BookSocial.comment_book',
    index=2,
    containing_service=None,
    input_type=_COMMENTBOOKREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_book_comment',
    full_name='book_social.BookSocial.get_book_comment',
    index=3,
    containing_service=None,
    input_type=_GETBOOKCOMMENTREQUEST,
    output_type=_GETBOOKCOMMENTLISTRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKSOCIAL)

DESCRIPTOR.services_by_name['BookSocial'] = _BOOKSOCIAL

# @@protoc_insertion_point(module_scope)
