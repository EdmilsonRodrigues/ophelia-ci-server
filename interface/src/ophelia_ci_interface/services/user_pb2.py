# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user.proto
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
    'user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ophelia_ci_interface.services.common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\x1a\x0c\x63ommon.proto\"2\n\x1e\x41uthenticationChallengeRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"4\n\x1f\x41uthenticationChallengeResponse\x12\x11\n\tchallenge\x18\x01 \x01(\t\"<\n\x15\x41uthenticationRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x11\n\tchallenge\x18\x02 \x01(\t\">\n\x16\x41uthenticationResponse\x12\x15\n\rauthenticated\x18\x01 \x01(\x08\x12\r\n\x05token\x18\x02 \x01(\t\".\n\x0eGetUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"8\n\x11\x43reateUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x11\n\tpublicKey\x18\x02 \x01(\t\"D\n\x11UpdateUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x11\n\tpublicKey\x18\x03 \x01(\t\",\n\x0cUserResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"5\n\x10ListUserResponse\x12!\n\x05users\x18\x01 \x03(\x0b\x32\x12.user.UserResponse\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\t2\xc2\x01\n\x0b\x41uthService\x12\x66\n\x17\x41uthenticationChallenge\x12$.user.AuthenticationChallengeRequest\x1a%.user.AuthenticationChallengeResponse\x12K\n\x0e\x41uthentication\x12\x1b.user.AuthenticationRequest\x1a\x1c.user.AuthenticationResponse2\xa1\x02\n\x0bUserService\x12\x39\n\nCreateUser\x12\x17.user.CreateUserRequest\x1a\x12.user.UserResponse\x12\x39\n\nUpdateUser\x12\x17.user.UpdateUserRequest\x1a\x12.user.UserResponse\x12\x31\n\x08ListUser\x12\r.common.Empty\x1a\x16.user.ListUserResponse\x12\x33\n\x07GetUser\x12\x14.user.GetUserRequest\x1a\x12.user.UserResponse\x12\x34\n\nDeleteUser\x12\x17.user.DeleteUserRequest\x1a\r.common.EmptyB)Z\'github.com/EdmilsonRodrigues/ophelia-cib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/EdmilsonRodrigues/ophelia-ci'
  _globals['_AUTHENTICATIONCHALLENGEREQUEST']._serialized_start=34
  _globals['_AUTHENTICATIONCHALLENGEREQUEST']._serialized_end=84
  _globals['_AUTHENTICATIONCHALLENGERESPONSE']._serialized_start=86
  _globals['_AUTHENTICATIONCHALLENGERESPONSE']._serialized_end=138
  _globals['_AUTHENTICATIONREQUEST']._serialized_start=140
  _globals['_AUTHENTICATIONREQUEST']._serialized_end=200
  _globals['_AUTHENTICATIONRESPONSE']._serialized_start=202
  _globals['_AUTHENTICATIONRESPONSE']._serialized_end=264
  _globals['_GETUSERREQUEST']._serialized_start=266
  _globals['_GETUSERREQUEST']._serialized_end=312
  _globals['_CREATEUSERREQUEST']._serialized_start=314
  _globals['_CREATEUSERREQUEST']._serialized_end=370
  _globals['_UPDATEUSERREQUEST']._serialized_start=372
  _globals['_UPDATEUSERREQUEST']._serialized_end=440
  _globals['_USERRESPONSE']._serialized_start=442
  _globals['_USERRESPONSE']._serialized_end=486
  _globals['_LISTUSERRESPONSE']._serialized_start=488
  _globals['_LISTUSERRESPONSE']._serialized_end=541
  _globals['_DELETEUSERREQUEST']._serialized_start=543
  _globals['_DELETEUSERREQUEST']._serialized_end=574
  _globals['_AUTHSERVICE']._serialized_start=577
  _globals['_AUTHSERVICE']._serialized_end=771
  _globals['_USERSERVICE']._serialized_start=774
  _globals['_USERSERVICE']._serialized_end=1063
# @@protoc_insertion_point(module_scope)
