# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: person.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'person.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cperson.proto\"X\n\rPersonMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\"\x07\n\x05\x45mpty\"4\n\x11PersonMessageList\x12\x1f\n\x07persons\x18\x01 \x03(\x0b\x32\x0e.PersonMessage29\n\rPersonService\x12(\n\nGetPersons\x12\x06.Empty\x1a\x12.PersonMessageListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'person_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PERSONMESSAGE']._serialized_start=16
  _globals['_PERSONMESSAGE']._serialized_end=104
  _globals['_EMPTY']._serialized_start=106
  _globals['_EMPTY']._serialized_end=113
  _globals['_PERSONMESSAGELIST']._serialized_start=115
  _globals['_PERSONMESSAGELIST']._serialized_end=167
  _globals['_PERSONSERVICE']._serialized_start=169
  _globals['_PERSONSERVICE']._serialized_end=226
# @@protoc_insertion_point(module_scope)
