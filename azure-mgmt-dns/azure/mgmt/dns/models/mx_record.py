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


class MxRecord(Model):
    """An MX record.

    :param preference: The preference value for this MX record.
    :type preference: int
    :param exchange: The domain name of the mail host for this MX record.
    :type exchange: str
    """

    _attribute_map = {
        'preference': {'key': 'preference', 'type': 'int'},
        'exchange': {'key': 'exchange', 'type': 'str'},
    }

    def __init__(self, preference=None, exchange=None):
        super(MxRecord, self).__init__()
        self.preference = preference
        self.exchange = exchange
