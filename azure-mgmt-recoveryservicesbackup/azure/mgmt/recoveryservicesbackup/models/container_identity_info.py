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


class ContainerIdentityInfo(Model):
    """Container identity information.

    :param unique_name: Unique name of the container
    :type unique_name: str
    :param aad_tenant_id: Protection container identity - AAD Tenant
    :type aad_tenant_id: str
    :param service_principal_client_id: Protection container identity - AAD
     Service Principal
    :type service_principal_client_id: str
    :param audience: Protection container identity - Audience
    :type audience: str
    """

    _attribute_map = {
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'aad_tenant_id': {'key': 'aadTenantId', 'type': 'str'},
        'service_principal_client_id': {'key': 'servicePrincipalClientId', 'type': 'str'},
        'audience': {'key': 'audience', 'type': 'str'},
    }

    def __init__(self, unique_name=None, aad_tenant_id=None, service_principal_client_id=None, audience=None):
        super(ContainerIdentityInfo, self).__init__()
        self.unique_name = unique_name
        self.aad_tenant_id = aad_tenant_id
        self.service_principal_client_id = service_principal_client_id
        self.audience = audience