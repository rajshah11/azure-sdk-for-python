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


class ClusterHealthChunk(Model):
    """Represents the health chunk of the cluster.
    Contains the cluster aggregated health state, and the cluster entities that
    respect the input filter.
    .

    :param health_state: Possible values include: 'Invalid', 'Ok', 'Warning',
     'Error', 'Unknown'
    :type health_state: str or ~azure.servicefabric.models.enum
    :param node_health_state_chunks:
    :type node_health_state_chunks:
     ~azure.servicefabric.models.NodeHealthStateChunkList
    :param application_health_state_chunks:
    :type application_health_state_chunks:
     ~azure.servicefabric.models.ApplicationHealthStateChunkList
    """

    _attribute_map = {
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'node_health_state_chunks': {'key': 'NodeHealthStateChunks', 'type': 'NodeHealthStateChunkList'},
        'application_health_state_chunks': {'key': 'ApplicationHealthStateChunks', 'type': 'ApplicationHealthStateChunkList'},
    }

    def __init__(self, health_state=None, node_health_state_chunks=None, application_health_state_chunks=None):
        super(ClusterHealthChunk, self).__init__()
        self.health_state = health_state
        self.node_health_state_chunks = node_health_state_chunks
        self.application_health_state_chunks = application_health_state_chunks
