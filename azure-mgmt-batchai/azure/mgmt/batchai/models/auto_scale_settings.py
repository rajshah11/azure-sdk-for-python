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


class AutoScaleSettings(Model):
    """The system automatically scales the cluster up and down (within
    minimumNodeCount and maximumNodeCount) based on the pending and running
    jobs on the cluster.

    :param minimum_node_count: Specifies the minimum number of compute nodes
     the cluster can have.
    :type minimum_node_count: int
    :param maximum_node_count: Specifies the maximum number of compute nodes
     the cluster can have.
    :type maximum_node_count: int
    :param initial_node_count: Specifies the number of compute nodes to
     allocate on cluster creation. Note that this value is used only during
     cluster creation.  Default value: 0 .
    :type initial_node_count: int
    """

    _validation = {
        'minimum_node_count': {'required': True},
        'maximum_node_count': {'required': True},
    }

    _attribute_map = {
        'minimum_node_count': {'key': 'minimumNodeCount', 'type': 'int'},
        'maximum_node_count': {'key': 'maximumNodeCount', 'type': 'int'},
        'initial_node_count': {'key': 'initialNodeCount', 'type': 'int'},
    }

    def __init__(self, minimum_node_count, maximum_node_count, initial_node_count=0):
        super(AutoScaleSettings, self).__init__()
        self.minimum_node_count = minimum_node_count
        self.maximum_node_count = maximum_node_count
        self.initial_node_count = initial_node_count
