# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: health.proto
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
    'health.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ophelia_ci_interface.services.common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0chealth.proto\x12\x06health\x1a\x0c\x63ommon.proto27\n\rHealthService\x12&\n\x06Health\x12\r.common.Empty\x1a\r.common.EmptyB)Z\'github.com/EdmilsonRodrigues/ophelia-cib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'health_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/EdmilsonRodrigues/ophelia-ci'
  _globals['_HEALTHSERVICE']._serialized_start=38
  _globals['_HEALTHSERVICE']._serialized_end=93
# @@protoc_insertion_point(module_scope)
