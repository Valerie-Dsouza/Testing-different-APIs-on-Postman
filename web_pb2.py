# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: web.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tweb.proto\x12\x04webs\".\n\rWebAppRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2B\n\nWebService\x12\x34\n\x06WebApp\x12\x13.webs.WebAppRequest\x1a\x13.webs.WebAppRequest\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'web_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_WEBAPPREQUEST']._serialized_start=19
  _globals['_WEBAPPREQUEST']._serialized_end=65
  _globals['_WEBSERVICE']._serialized_start=67
  _globals['_WEBSERVICE']._serialized_end=133
# @@protoc_insertion_point(module_scope)
