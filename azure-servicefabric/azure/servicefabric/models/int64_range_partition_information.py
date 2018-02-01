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

from .partition_information import PartitionInformation


class Int64RangePartitionInformation(PartitionInformation):
    """Describes the partition information for the integer range that is based on
    partition schemes.

    :param id:
    :type id: str
    :param service_partition_kind: Constant filled by server.
    :type service_partition_kind: str
    :param low_key: Specifies the minimum key value handled by this partition.
    :type low_key: str
    :param high_key: Specifies the maximum key value handled by this
     partition.
    :type high_key: str
    """

    _validation = {
        'service_partition_kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'service_partition_kind': {'key': 'ServicePartitionKind', 'type': 'str'},
        'low_key': {'key': 'LowKey', 'type': 'str'},
        'high_key': {'key': 'HighKey', 'type': 'str'},
    }

    def __init__(self, id=None, low_key=None, high_key=None):
        super(Int64RangePartitionInformation, self).__init__(id=id)
        self.low_key = low_key
        self.high_key = high_key
        self.service_partition_kind = 'Int64Range'
