# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/schemas/ga4gh/allele_annotations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh.schemas.ga4gh import common_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/schemas/ga4gh/allele_annotations.proto',
  package='ga4gh.schemas.ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n,ga4gh/schemas/ga4gh/allele_annotations.proto\x12\x13ga4gh.schemas.ga4gh\x1a ga4gh/schemas/ga4gh/common.proto\"D\n\x0e\x41nalysisResult\x12\x13\n\x0b\x61nalysis_id\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x05\"d\n\x0e\x41lleleLocation\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\x12\x1a\n\x12reference_sequence\x18\x03 \x01(\t\x12\x1a\n\x12\x61lternate_sequence\x18\x04 \x01(\t\"\xae\x01\n\x14VariantAnnotationSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0evariant_set_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12/\n\x08\x61nalysis\x18\x04 \x01(\x0b\x32\x1d.ga4gh.schemas.ga4gh.Analysis\x12\x33\n\nattributes\x18\x05 \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\"F\n\x0eHGVSAnnotation\x12\x0f\n\x07genomic\x18\x01 \x01(\t\x12\x12\n\ntranscript\x18\x02 \x01(\t\x12\x0f\n\x07protein\x18\x03 \x01(\t\"\xe7\x03\n\x10TranscriptEffect\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nfeature_id\x18\x02 \x01(\t\x12\x17\n\x0f\x61lternate_bases\x18\x03 \x01(\t\x12\x32\n\x07\x65\x66\x66\x65\x63ts\x18\x04 \x03(\x0b\x32!.ga4gh.schemas.ga4gh.OntologyTerm\x12<\n\x0fhgvs_annotation\x18\x05 \x01(\x0b\x32#.ga4gh.schemas.ga4gh.HGVSAnnotation\x12:\n\rcdna_location\x18\x06 \x01(\x0b\x32#.ga4gh.schemas.ga4gh.AlleleLocation\x12\x39\n\x0c\x63\x64s_location\x18\x07 \x01(\x0b\x32#.ga4gh.schemas.ga4gh.AlleleLocation\x12=\n\x10protein_location\x18\x08 \x01(\x0b\x32#.ga4gh.schemas.ga4gh.AlleleLocation\x12=\n\x10\x61nalysis_results\x18\t \x03(\x0b\x32#.ga4gh.schemas.ga4gh.AnalysisResult\x12\x33\n\nattributes\x18\x0b \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\"\xdf\x01\n\x11VariantAnnotation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nvariant_id\x18\x02 \x01(\t\x12!\n\x19variant_annotation_set_id\x18\x03 \x01(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\t\x12\x41\n\x12transcript_effects\x18\x05 \x03(\x0b\x32%.ga4gh.schemas.ga4gh.TranscriptEffect\x12\x33\n\nattributes\x18\x07 \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributesb\x06proto3')
  ,
  dependencies=[ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ANALYSISRESULT = _descriptor.Descriptor(
  name='AnalysisResult',
  full_name='ga4gh.schemas.ga4gh.AnalysisResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analysis_id', full_name='ga4gh.schemas.ga4gh.AnalysisResult.analysis_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='ga4gh.schemas.ga4gh.AnalysisResult.result', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='ga4gh.schemas.ga4gh.AnalysisResult.score', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=171,
)


_ALLELELOCATION = _descriptor.Descriptor(
  name='AlleleLocation',
  full_name='ga4gh.schemas.ga4gh.AlleleLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh.schemas.ga4gh.AlleleLocation.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='ga4gh.schemas.ga4gh.AlleleLocation.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_sequence', full_name='ga4gh.schemas.ga4gh.AlleleLocation.reference_sequence', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternate_sequence', full_name='ga4gh.schemas.ga4gh.AlleleLocation.alternate_sequence', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=273,
)


_VARIANTANNOTATIONSET = _descriptor.Descriptor(
  name='VariantAnnotationSet',
  full_name='ga4gh.schemas.ga4gh.VariantAnnotationSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.VariantAnnotationSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_set_id', full_name='ga4gh.schemas.ga4gh.VariantAnnotationSet.variant_set_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.VariantAnnotationSet.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analysis', full_name='ga4gh.schemas.ga4gh.VariantAnnotationSet.analysis', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.VariantAnnotationSet.attributes', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=450,
)


_HGVSANNOTATION = _descriptor.Descriptor(
  name='HGVSAnnotation',
  full_name='ga4gh.schemas.ga4gh.HGVSAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='genomic', full_name='ga4gh.schemas.ga4gh.HGVSAnnotation.genomic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transcript', full_name='ga4gh.schemas.ga4gh.HGVSAnnotation.transcript', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protein', full_name='ga4gh.schemas.ga4gh.HGVSAnnotation.protein', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=522,
)


_TRANSCRIPTEFFECT = _descriptor.Descriptor(
  name='TranscriptEffect',
  full_name='ga4gh.schemas.ga4gh.TranscriptEffect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.TranscriptEffect.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_id', full_name='ga4gh.schemas.ga4gh.TranscriptEffect.feature_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternate_bases', full_name='ga4gh.schemas.ga4gh.TranscriptEffect.alternate_bases', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effects', full_name='ga4gh.schemas.ga4gh.TranscriptEffect.effects', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hgvs_annotation', full_name='ga4gh.schemas.ga4gh.TranscriptEffect.hgvs_annotation', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cdna_location', full_name='ga4gh.schemas.ga4gh.TranscriptEffect.cdna_location', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cds_location', full_name='ga4gh.schemas.ga4gh.TranscriptEffect.cds_location', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protein_location', full_name='ga4gh.schemas.ga4gh.TranscriptEffect.protein_location', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analysis_results', full_name='ga4gh.schemas.ga4gh.TranscriptEffect.analysis_results', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.TranscriptEffect.attributes', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=525,
  serialized_end=1012,
)


_VARIANTANNOTATION = _descriptor.Descriptor(
  name='VariantAnnotation',
  full_name='ga4gh.schemas.ga4gh.VariantAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.VariantAnnotation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_id', full_name='ga4gh.schemas.ga4gh.VariantAnnotation.variant_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_annotation_set_id', full_name='ga4gh.schemas.ga4gh.VariantAnnotation.variant_annotation_set_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='ga4gh.schemas.ga4gh.VariantAnnotation.created', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transcript_effects', full_name='ga4gh.schemas.ga4gh.VariantAnnotation.transcript_effects', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.VariantAnnotation.attributes', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1015,
  serialized_end=1238,
)

_VARIANTANNOTATIONSET.fields_by_name['analysis'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ANALYSIS
_VARIANTANNOTATIONSET.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
_TRANSCRIPTEFFECT.fields_by_name['effects'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ONTOLOGYTERM
_TRANSCRIPTEFFECT.fields_by_name['hgvs_annotation'].message_type = _HGVSANNOTATION
_TRANSCRIPTEFFECT.fields_by_name['cdna_location'].message_type = _ALLELELOCATION
_TRANSCRIPTEFFECT.fields_by_name['cds_location'].message_type = _ALLELELOCATION
_TRANSCRIPTEFFECT.fields_by_name['protein_location'].message_type = _ALLELELOCATION
_TRANSCRIPTEFFECT.fields_by_name['analysis_results'].message_type = _ANALYSISRESULT
_TRANSCRIPTEFFECT.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
_VARIANTANNOTATION.fields_by_name['transcript_effects'].message_type = _TRANSCRIPTEFFECT
_VARIANTANNOTATION.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
DESCRIPTOR.message_types_by_name['AnalysisResult'] = _ANALYSISRESULT
DESCRIPTOR.message_types_by_name['AlleleLocation'] = _ALLELELOCATION
DESCRIPTOR.message_types_by_name['VariantAnnotationSet'] = _VARIANTANNOTATIONSET
DESCRIPTOR.message_types_by_name['HGVSAnnotation'] = _HGVSANNOTATION
DESCRIPTOR.message_types_by_name['TranscriptEffect'] = _TRANSCRIPTEFFECT
DESCRIPTOR.message_types_by_name['VariantAnnotation'] = _VARIANTANNOTATION

AnalysisResult = _reflection.GeneratedProtocolMessageType('AnalysisResult', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSISRESULT,
  __module__ = 'ga4gh.schemas.ga4gh.allele_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.AnalysisResult)
  ))
_sym_db.RegisterMessage(AnalysisResult)

AlleleLocation = _reflection.GeneratedProtocolMessageType('AlleleLocation', (_message.Message,), dict(
  DESCRIPTOR = _ALLELELOCATION,
  __module__ = 'ga4gh.schemas.ga4gh.allele_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.AlleleLocation)
  ))
_sym_db.RegisterMessage(AlleleLocation)

VariantAnnotationSet = _reflection.GeneratedProtocolMessageType('VariantAnnotationSet', (_message.Message,), dict(
  DESCRIPTOR = _VARIANTANNOTATIONSET,
  __module__ = 'ga4gh.schemas.ga4gh.allele_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.VariantAnnotationSet)
  ))
_sym_db.RegisterMessage(VariantAnnotationSet)

HGVSAnnotation = _reflection.GeneratedProtocolMessageType('HGVSAnnotation', (_message.Message,), dict(
  DESCRIPTOR = _HGVSANNOTATION,
  __module__ = 'ga4gh.schemas.ga4gh.allele_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.HGVSAnnotation)
  ))
_sym_db.RegisterMessage(HGVSAnnotation)

TranscriptEffect = _reflection.GeneratedProtocolMessageType('TranscriptEffect', (_message.Message,), dict(
  DESCRIPTOR = _TRANSCRIPTEFFECT,
  __module__ = 'ga4gh.schemas.ga4gh.allele_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.TranscriptEffect)
  ))
_sym_db.RegisterMessage(TranscriptEffect)

VariantAnnotation = _reflection.GeneratedProtocolMessageType('VariantAnnotation', (_message.Message,), dict(
  DESCRIPTOR = _VARIANTANNOTATION,
  __module__ = 'ga4gh.schemas.ga4gh.allele_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.VariantAnnotation)
  ))
_sym_db.RegisterMessage(VariantAnnotation)


# @@protoc_insertion_point(module_scope)
