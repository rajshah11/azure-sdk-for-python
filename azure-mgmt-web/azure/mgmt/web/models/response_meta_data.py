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


class ResponseMetaData(Model):
    """ResponseMetaData.

    :param data_source: Source of the Data
    :type data_source: ~azure.mgmt.web.models.DataSource
    """

    _attribute_map = {
        'data_source': {'key': 'dataSource', 'type': 'DataSource'},
    }

    def __init__(self, data_source=None):
        super(ResponseMetaData, self).__init__()
        self.data_source = data_source
