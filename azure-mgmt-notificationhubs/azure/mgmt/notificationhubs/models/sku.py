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


class Sku(Model):
    """The Sku description for a namespace.

    :param name: Name of the notification hub sku. Possible values include:
     'Free', 'Basic', 'Standard'
    :type name: str or ~azure.mgmt.notificationhubs.models.SkuName
    :param tier: The tier of particular sku
    :type tier: str
    :param size: The Sku size
    :type size: str
    :param family: The Sku Family
    :type family: str
    :param capacity: The capacity of the resource
    :type capacity: int
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, name, tier=None, size=None, family=None, capacity=None):
        super(Sku, self).__init__()
        self.name = name
        self.tier = tier
        self.size = size
        self.family = family
        self.capacity = capacity
