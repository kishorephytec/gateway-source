# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generic_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import config_message_pb2 as config__message__pb2
import data_message_pb2 as data__message__pb2
import otap_message_pb2 as otap__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='generic_message.proto',
  package='wirepas.proto.gateway_api',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15generic_message.proto\x12\x19wirepas.proto.gateway_api\x1a\x14\x63onfig_message.proto\x1a\x12\x64\x61ta_message.proto\x1a\x12otap_message.proto\"\x89\x0b\n\x0eWirepasMessage\x12<\n\x0cstatus_event\x18\x01 \x01(\x0b\x32&.wirepas.proto.gateway_api.StatusEvent\x12\x41\n\x0fget_configs_req\x18\x02 \x01(\x0b\x32(.wirepas.proto.gateway_api.GetConfigsReq\x12\x43\n\x10get_configs_resp\x18\x03 \x01(\x0b\x32).wirepas.proto.gateway_api.GetConfigsResp\x12?\n\x0eset_config_req\x18\x04 \x01(\x0b\x32\'.wirepas.proto.gateway_api.SetConfigReq\x12\x41\n\x0fset_config_resp\x18\x05 \x01(\x0b\x32(.wirepas.proto.gateway_api.SetConfigResp\x12\x41\n\x0fsend_packet_req\x18\x06 \x01(\x0b\x32(.wirepas.proto.gateway_api.SendPacketReq\x12\x43\n\x10send_packet_resp\x18\x07 \x01(\x0b\x32).wirepas.proto.gateway_api.SendPacketResp\x12M\n\x15packet_received_event\x18\x08 \x01(\x0b\x32..wirepas.proto.gateway_api.PacketReceivedEvent\x12T\n\x19get_scratchpad_status_req\x18\t \x01(\x0b\x32\x31.wirepas.proto.gateway_api.GetScratchpadStatusReq\x12V\n\x1aget_scratchpad_status_resp\x18\n \x01(\x0b\x32\x32.wirepas.proto.gateway_api.GetScratchpadStatusResp\x12M\n\x15upload_scratchpad_req\x18\x0b \x01(\x0b\x32..wirepas.proto.gateway_api.UploadScratchpadReq\x12O\n\x16upload_scratchpad_resp\x18\x0c \x01(\x0b\x32/.wirepas.proto.gateway_api.UploadScratchpadResp\x12O\n\x16process_scratchpad_req\x18\r \x01(\x0b\x32/.wirepas.proto.gateway_api.ProcessScratchpadReq\x12Q\n\x17process_scratchpad_resp\x18\x0e \x01(\x0b\x32\x30.wirepas.proto.gateway_api.ProcessScratchpadResp\x12\x45\n\x14get_gateway_info_req\x18\x0f \x01(\x0b\x32\'.wirepas.proto.gateway_api.GetGwInfoReq\x12G\n\x15get_gateway_info_resp\x18\x10 \x01(\x0b\x32(.wirepas.proto.gateway_api.GetGwInfoResp\x12h\n$set_scratchpad_target_and_action_req\x18\x11 \x01(\x0b\x32:.wirepas.proto.gateway_api.SetScratchpadTargetAndActionReq\x12j\n%set_scratchpad_target_and_action_resp\x18\x12 \x01(\x0b\x32;.wirepas.proto.gateway_api.SetScratchpadTargetAndActionResp\"(\n\x0f\x43ustomerMessage\x12\x15\n\rcustomer_name\x18\x01 \x02(\t\"\x8a\x01\n\x0eGenericMessage\x12:\n\x07wirepas\x18\x01 \x01(\x0b\x32).wirepas.proto.gateway_api.WirepasMessage\x12<\n\x08\x63ustomer\x18\x02 \x01(\x0b\x32*.wirepas.proto.gateway_api.CustomerMessage'
  ,
  dependencies=[config__message__pb2.DESCRIPTOR,data__message__pb2.DESCRIPTOR,otap__message__pb2.DESCRIPTOR,])




_WIREPASMESSAGE = _descriptor.Descriptor(
  name='WirepasMessage',
  full_name='wirepas.proto.gateway_api.WirepasMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_event', full_name='wirepas.proto.gateway_api.WirepasMessage.status_event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_configs_req', full_name='wirepas.proto.gateway_api.WirepasMessage.get_configs_req', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_configs_resp', full_name='wirepas.proto.gateway_api.WirepasMessage.get_configs_resp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='set_config_req', full_name='wirepas.proto.gateway_api.WirepasMessage.set_config_req', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='set_config_resp', full_name='wirepas.proto.gateway_api.WirepasMessage.set_config_resp', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='send_packet_req', full_name='wirepas.proto.gateway_api.WirepasMessage.send_packet_req', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='send_packet_resp', full_name='wirepas.proto.gateway_api.WirepasMessage.send_packet_resp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packet_received_event', full_name='wirepas.proto.gateway_api.WirepasMessage.packet_received_event', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_scratchpad_status_req', full_name='wirepas.proto.gateway_api.WirepasMessage.get_scratchpad_status_req', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_scratchpad_status_resp', full_name='wirepas.proto.gateway_api.WirepasMessage.get_scratchpad_status_resp', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upload_scratchpad_req', full_name='wirepas.proto.gateway_api.WirepasMessage.upload_scratchpad_req', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upload_scratchpad_resp', full_name='wirepas.proto.gateway_api.WirepasMessage.upload_scratchpad_resp', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='process_scratchpad_req', full_name='wirepas.proto.gateway_api.WirepasMessage.process_scratchpad_req', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='process_scratchpad_resp', full_name='wirepas.proto.gateway_api.WirepasMessage.process_scratchpad_resp', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_gateway_info_req', full_name='wirepas.proto.gateway_api.WirepasMessage.get_gateway_info_req', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_gateway_info_resp', full_name='wirepas.proto.gateway_api.WirepasMessage.get_gateway_info_resp', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='set_scratchpad_target_and_action_req', full_name='wirepas.proto.gateway_api.WirepasMessage.set_scratchpad_target_and_action_req', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='set_scratchpad_target_and_action_resp', full_name='wirepas.proto.gateway_api.WirepasMessage.set_scratchpad_target_and_action_resp', index=17,
      number=18, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=1532,
)


_CUSTOMERMESSAGE = _descriptor.Descriptor(
  name='CustomerMessage',
  full_name='wirepas.proto.gateway_api.CustomerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_name', full_name='wirepas.proto.gateway_api.CustomerMessage.customer_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1534,
  serialized_end=1574,
)


_GENERICMESSAGE = _descriptor.Descriptor(
  name='GenericMessage',
  full_name='wirepas.proto.gateway_api.GenericMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='wirepas', full_name='wirepas.proto.gateway_api.GenericMessage.wirepas', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer', full_name='wirepas.proto.gateway_api.GenericMessage.customer', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1577,
  serialized_end=1715,
)

_WIREPASMESSAGE.fields_by_name['status_event'].message_type = config__message__pb2._STATUSEVENT
_WIREPASMESSAGE.fields_by_name['get_configs_req'].message_type = config__message__pb2._GETCONFIGSREQ
_WIREPASMESSAGE.fields_by_name['get_configs_resp'].message_type = config__message__pb2._GETCONFIGSRESP
_WIREPASMESSAGE.fields_by_name['set_config_req'].message_type = config__message__pb2._SETCONFIGREQ
_WIREPASMESSAGE.fields_by_name['set_config_resp'].message_type = config__message__pb2._SETCONFIGRESP
_WIREPASMESSAGE.fields_by_name['send_packet_req'].message_type = data__message__pb2._SENDPACKETREQ
_WIREPASMESSAGE.fields_by_name['send_packet_resp'].message_type = data__message__pb2._SENDPACKETRESP
_WIREPASMESSAGE.fields_by_name['packet_received_event'].message_type = data__message__pb2._PACKETRECEIVEDEVENT
_WIREPASMESSAGE.fields_by_name['get_scratchpad_status_req'].message_type = otap__message__pb2._GETSCRATCHPADSTATUSREQ
_WIREPASMESSAGE.fields_by_name['get_scratchpad_status_resp'].message_type = otap__message__pb2._GETSCRATCHPADSTATUSRESP
_WIREPASMESSAGE.fields_by_name['upload_scratchpad_req'].message_type = otap__message__pb2._UPLOADSCRATCHPADREQ
_WIREPASMESSAGE.fields_by_name['upload_scratchpad_resp'].message_type = otap__message__pb2._UPLOADSCRATCHPADRESP
_WIREPASMESSAGE.fields_by_name['process_scratchpad_req'].message_type = otap__message__pb2._PROCESSSCRATCHPADREQ
_WIREPASMESSAGE.fields_by_name['process_scratchpad_resp'].message_type = otap__message__pb2._PROCESSSCRATCHPADRESP
_WIREPASMESSAGE.fields_by_name['get_gateway_info_req'].message_type = config__message__pb2._GETGWINFOREQ
_WIREPASMESSAGE.fields_by_name['get_gateway_info_resp'].message_type = config__message__pb2._GETGWINFORESP
_WIREPASMESSAGE.fields_by_name['set_scratchpad_target_and_action_req'].message_type = otap__message__pb2._SETSCRATCHPADTARGETANDACTIONREQ
_WIREPASMESSAGE.fields_by_name['set_scratchpad_target_and_action_resp'].message_type = otap__message__pb2._SETSCRATCHPADTARGETANDACTIONRESP
_GENERICMESSAGE.fields_by_name['wirepas'].message_type = _WIREPASMESSAGE
_GENERICMESSAGE.fields_by_name['customer'].message_type = _CUSTOMERMESSAGE
DESCRIPTOR.message_types_by_name['WirepasMessage'] = _WIREPASMESSAGE
DESCRIPTOR.message_types_by_name['CustomerMessage'] = _CUSTOMERMESSAGE
DESCRIPTOR.message_types_by_name['GenericMessage'] = _GENERICMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WirepasMessage = _reflection.GeneratedProtocolMessageType('WirepasMessage', (_message.Message,), {
  'DESCRIPTOR' : _WIREPASMESSAGE,
  '__module__' : 'generic_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.WirepasMessage)
  })
_sym_db.RegisterMessage(WirepasMessage)

CustomerMessage = _reflection.GeneratedProtocolMessageType('CustomerMessage', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERMESSAGE,
  '__module__' : 'generic_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.CustomerMessage)
  })
_sym_db.RegisterMessage(CustomerMessage)

GenericMessage = _reflection.GeneratedProtocolMessageType('GenericMessage', (_message.Message,), {
  'DESCRIPTOR' : _GENERICMESSAGE,
  '__module__' : 'generic_message_pb2'
  # @@protoc_insertion_point(class_scope:wirepas.proto.gateway_api.GenericMessage)
  })
_sym_db.RegisterMessage(GenericMessage)


# @@protoc_insertion_point(module_scope)
