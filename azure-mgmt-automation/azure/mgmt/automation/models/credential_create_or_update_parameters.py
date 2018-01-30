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


class CredentialCreateOrUpdateParameters(Model):
    """The parameters supplied to the create or update credential operation.

    :param name: Gets or sets the name of the credential.
    :type name: str
    :param user_name: Gets or sets the user name of the credential.
    :type user_name: str
    :param password: Gets or sets the password of the credential.
    :type password: str
    :param description: Gets or sets the description of the credential.
    :type description: str
    """

    _validation = {
        'name': {'required': True},
        'user_name': {'required': True},
        'password': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
    }

    def __init__(self, name, user_name, password, description=None):
        super(CredentialCreateOrUpdateParameters, self).__init__()
        self.name = name
        self.user_name = user_name
        self.password = password
        self.description = description
