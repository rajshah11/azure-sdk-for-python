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


class HttpRequest(Model):
    """HttpRequest.

    :param authentication: Gets or sets the authentication method of the
     request.
    :type authentication: ~azure.mgmt.scheduler.models.HttpAuthentication
    :param uri: Gets or sets the URI of the request.
    :type uri: str
    :param method: Gets or sets the method of the request.
    :type method: str
    :param body: Gets or sets the request body.
    :type body: str
    :param headers: Gets or sets the headers.
    :type headers: dict[str, str]
    """

    _attribute_map = {
        'authentication': {'key': 'authentication', 'type': 'HttpAuthentication'},
        'uri': {'key': 'uri', 'type': 'str'},
        'method': {'key': 'method', 'type': 'str'},
        'body': {'key': 'body', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '{str}'},
    }

    def __init__(self, authentication=None, uri=None, method=None, body=None, headers=None):
        super(HttpRequest, self).__init__()
        self.authentication = authentication
        self.uri = uri
        self.method = method
        self.body = body
        self.headers = headers
