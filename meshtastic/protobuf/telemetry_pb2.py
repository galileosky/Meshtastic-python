# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/protobuf/telemetry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#meshtastic/protobuf/telemetry.proto\x12\x13meshtastic.protobuf\"\x81\x01\n\rDeviceMetrics\x12\x15\n\rbattery_level\x18\x01 \x01(\r\x12\x0f\n\x07voltage\x18\x02 \x01(\x02\x12\x1b\n\x13\x63hannel_utilization\x18\x03 \x01(\x02\x12\x13\n\x0b\x61ir_util_tx\x18\x04 \x01(\x02\x12\x16\n\x0euptime_seconds\x18\x05 \x01(\r\"\xdc\x02\n\x12\x45nvironmentMetrics\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\x19\n\x11relative_humidity\x18\x02 \x01(\x02\x12\x1b\n\x13\x62\x61rometric_pressure\x18\x03 \x01(\x02\x12\x16\n\x0egas_resistance\x18\x04 \x01(\x02\x12\x0f\n\x07voltage\x18\x05 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x06 \x01(\x02\x12\x0b\n\x03iaq\x18\x07 \x01(\r\x12\x10\n\x08\x64istance\x18\x08 \x01(\x02\x12\x0b\n\x03lux\x18\t \x01(\x02\x12\x11\n\twhite_lux\x18\n \x01(\x02\x12\x0e\n\x06ir_lux\x18\x0b \x01(\x02\x12\x0e\n\x06uv_lux\x18\x0c \x01(\x02\x12\x16\n\x0ewind_direction\x18\r \x01(\r\x12\x12\n\nwind_speed\x18\x0e \x01(\x02\x12\x0e\n\x06weight\x18\x0f \x01(\x02\x12\x11\n\twind_gust\x18\x10 \x01(\x02\x12\x11\n\twind_lull\x18\x11 \x01(\x02\"\x8c\x01\n\x0cPowerMetrics\x12\x13\n\x0b\x63h1_voltage\x18\x01 \x01(\x02\x12\x13\n\x0b\x63h1_current\x18\x02 \x01(\x02\x12\x13\n\x0b\x63h2_voltage\x18\x03 \x01(\x02\x12\x13\n\x0b\x63h2_current\x18\x04 \x01(\x02\x12\x13\n\x0b\x63h3_voltage\x18\x05 \x01(\x02\x12\x13\n\x0b\x63h3_current\x18\x06 \x01(\x02\"\xbf\x02\n\x11\x41irQualityMetrics\x12\x15\n\rpm10_standard\x18\x01 \x01(\r\x12\x15\n\rpm25_standard\x18\x02 \x01(\r\x12\x16\n\x0epm100_standard\x18\x03 \x01(\r\x12\x1a\n\x12pm10_environmental\x18\x04 \x01(\r\x12\x1a\n\x12pm25_environmental\x18\x05 \x01(\r\x12\x1b\n\x13pm100_environmental\x18\x06 \x01(\r\x12\x16\n\x0eparticles_03um\x18\x07 \x01(\r\x12\x16\n\x0eparticles_05um\x18\x08 \x01(\r\x12\x16\n\x0eparticles_10um\x18\t \x01(\r\x12\x16\n\x0eparticles_25um\x18\n \x01(\r\x12\x16\n\x0eparticles_50um\x18\x0b \x01(\r\x12\x17\n\x0fparticles_100um\x18\x0c \x01(\r\"\xad\x02\n\tTelemetry\x12\x0c\n\x04time\x18\x01 \x01(\x07\x12<\n\x0e\x64\x65vice_metrics\x18\x02 \x01(\x0b\x32\".meshtastic.protobuf.DeviceMetricsH\x00\x12\x46\n\x13\x65nvironment_metrics\x18\x03 \x01(\x0b\x32\'.meshtastic.protobuf.EnvironmentMetricsH\x00\x12\x45\n\x13\x61ir_quality_metrics\x18\x04 \x01(\x0b\x32&.meshtastic.protobuf.AirQualityMetricsH\x00\x12:\n\rpower_metrics\x18\x05 \x01(\x0b\x32!.meshtastic.protobuf.PowerMetricsH\x00\x42\t\n\x07variant\">\n\rNau7802Config\x12\x12\n\nzeroOffset\x18\x01 \x01(\x05\x12\x19\n\x11\x63\x61librationFactor\x18\x02 \x01(\x02*\xea\x02\n\x13TelemetrySensorType\x12\x10\n\x0cSENSOR_UNSET\x10\x00\x12\n\n\x06\x42ME280\x10\x01\x12\n\n\x06\x42ME680\x10\x02\x12\x0b\n\x07MCP9808\x10\x03\x12\n\n\x06INA260\x10\x04\x12\n\n\x06INA219\x10\x05\x12\n\n\x06\x42MP280\x10\x06\x12\t\n\x05SHTC3\x10\x07\x12\t\n\x05LPS22\x10\x08\x12\x0b\n\x07QMC6310\x10\t\x12\x0b\n\x07QMI8658\x10\n\x12\x0c\n\x08QMC5883L\x10\x0b\x12\t\n\x05SHT31\x10\x0c\x12\x0c\n\x08PMSA003I\x10\r\x12\x0b\n\x07INA3221\x10\x0e\x12\n\n\x06\x42MP085\x10\x0f\x12\x0c\n\x08RCWL9620\x10\x10\x12\t\n\x05SHT4X\x10\x11\x12\x0c\n\x08VEML7700\x10\x12\x12\x0c\n\x08MLX90632\x10\x13\x12\x0b\n\x07OPT3001\x10\x14\x12\x0c\n\x08LTR390UV\x10\x15\x12\x0e\n\nTSL25911FN\x10\x16\x12\t\n\x05\x41HT10\x10\x17\x12\x10\n\x0c\x44\x46ROBOT_LARK\x10\x18\x12\x0b\n\x07NAU7802\x10\x19\x42\x64\n\x13\x63om.geeksville.meshB\x0fTelemetryProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.protobuf.telemetry_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\017TelemetryProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _globals['_TELEMETRYSENSORTYPE']._serialized_start=1377
  _globals['_TELEMETRYSENSORTYPE']._serialized_end=1739
  _globals['_DEVICEMETRICS']._serialized_start=61
  _globals['_DEVICEMETRICS']._serialized_end=190
  _globals['_ENVIRONMENTMETRICS']._serialized_start=193
  _globals['_ENVIRONMENTMETRICS']._serialized_end=541
  _globals['_POWERMETRICS']._serialized_start=544
  _globals['_POWERMETRICS']._serialized_end=684
  _globals['_AIRQUALITYMETRICS']._serialized_start=687
  _globals['_AIRQUALITYMETRICS']._serialized_end=1006
  _globals['_TELEMETRY']._serialized_start=1009
  _globals['_TELEMETRY']._serialized_end=1310
  _globals['_NAU7802CONFIG']._serialized_start=1312
  _globals['_NAU7802CONFIG']._serialized_end=1374
# @@protoc_insertion_point(module_scope)
