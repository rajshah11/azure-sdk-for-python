# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EdifactDelimiterOverride(Model):
    """The Edifact delimiter override settings.

    :param message_id: The message id.
    :type message_id: str
    :param message_version: The message version.
    :type message_version: str
    :param message_release: The message releaseversion.
    :type message_release: str
    :param data_element_separator: The data element separator.
    :type data_element_separator: int
    :param component_separator: The component separator.
    :type component_separator: int
    :param segment_terminator: The segment terminator.
    :type segment_terminator: int
    :param repetition_separator: The repetition separator.
    :type repetition_separator: int
    :param segment_terminator_suffix: The segment terminator suffix. Possible
     values include: 'NotSpecified', 'None', 'CR', 'LF', 'CRLF'
    :type segment_terminator_suffix: str or
     ~azure.mgmt.logic.models.SegmentTerminatorSuffix
    :param decimal_point_indicator: The decimal point indicator. Possible
     values include: 'NotSpecified', 'Comma', 'Decimal'
    :type decimal_point_indicator: str or
     ~azure.mgmt.logic.models.EdifactDecimalIndicator
    :param release_indicator: The release indicator.
    :type release_indicator: int
    :param message_association_assigned_code: The message association assigned
     code.
    :type message_association_assigned_code: str
    :param target_namespace: The target namespace on which this delimiter
     settings has to be applied.
    :type target_namespace: str
    """

    _validation = {
        'data_element_separator': {'required': True},
        'component_separator': {'required': True},
        'segment_terminator': {'required': True},
        'repetition_separator': {'required': True},
        'segment_terminator_suffix': {'required': True},
        'decimal_point_indicator': {'required': True},
        'release_indicator': {'required': True},
    }

    _attribute_map = {
        'message_id': {'key': 'messageId', 'type': 'str'},
        'message_version': {'key': 'messageVersion', 'type': 'str'},
        'message_release': {'key': 'messageRelease', 'type': 'str'},
        'data_element_separator': {'key': 'dataElementSeparator', 'type': 'int'},
        'component_separator': {'key': 'componentSeparator', 'type': 'int'},
        'segment_terminator': {'key': 'segmentTerminator', 'type': 'int'},
        'repetition_separator': {'key': 'repetitionSeparator', 'type': 'int'},
        'segment_terminator_suffix': {'key': 'segmentTerminatorSuffix', 'type': 'SegmentTerminatorSuffix'},
        'decimal_point_indicator': {'key': 'decimalPointIndicator', 'type': 'EdifactDecimalIndicator'},
        'release_indicator': {'key': 'releaseIndicator', 'type': 'int'},
        'message_association_assigned_code': {'key': 'messageAssociationAssignedCode', 'type': 'str'},
        'target_namespace': {'key': 'targetNamespace', 'type': 'str'},
    }

    def __init__(self, data_element_separator, component_separator, segment_terminator, repetition_separator, segment_terminator_suffix, decimal_point_indicator, release_indicator, message_id=None, message_version=None, message_release=None, message_association_assigned_code=None, target_namespace=None):
        super(EdifactDelimiterOverride, self).__init__()
        self.message_id = message_id
        self.message_version = message_version
        self.message_release = message_release
        self.data_element_separator = data_element_separator
        self.component_separator = component_separator
        self.segment_terminator = segment_terminator
        self.repetition_separator = repetition_separator
        self.segment_terminator_suffix = segment_terminator_suffix
        self.decimal_point_indicator = decimal_point_indicator
        self.release_indicator = release_indicator
        self.message_association_assigned_code = message_association_assigned_code
        self.target_namespace = target_namespace
