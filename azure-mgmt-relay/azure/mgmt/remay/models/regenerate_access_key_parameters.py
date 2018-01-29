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


class RegenerateAccessKeyParameters(Model):
    """Parameters supplied to the regenerate authorization rule operation,
    specifies which key neeeds to be reset.

    :param key_type: The access key to regenerate. Possible values include:
     'PrimaryKey', 'SecondaryKey'
    :type key_type: str or ~azure.mgmt.relay.models.KeyType
    :param key: Optional. If the key value is provided, this is set to key
     type, or autogenerated key value set for key type.
    :type key: str
    """

    _validation = {
        'key_type': {'required': True},
    }

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'KeyType'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(self, key_type, key=None):
        super(RegenerateAccessKeyParameters, self).__init__()
        self.key_type = key_type
        self.key = key