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


class EdifactMessageIdentifier(Model):
    """The Edifact message identifier.

    :param message_id: The message id on which this envelope settings has to
     be applied.
    :type message_id: str
    """

    _validation = {
        'message_id': {'required': True},
    }

    _attribute_map = {
        'message_id': {'key': 'messageId', 'type': 'str'},
    }

    def __init__(self, message_id):
        super(EdifactMessageIdentifier, self).__init__()
        self.message_id = message_id
