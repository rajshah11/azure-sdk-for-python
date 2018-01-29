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


class RestartDeployedCodePackageDescription(Model):
    """Defines description for restarting a deloyed code package on Service Fabric
    node.
    .

    :param service_manifest_name:
    :type service_manifest_name: str
    :param service_package_activation_id:
    :type service_package_activation_id: str
    :param code_package_name:
    :type code_package_name: str
    :param code_package_instance_id:
    :type code_package_instance_id: str
    """

    _validation = {
        'service_manifest_name': {'required': True},
        'code_package_name': {'required': True},
        'code_package_instance_id': {'required': True},
    }

    _attribute_map = {
        'service_manifest_name': {'key': 'ServiceManifestName', 'type': 'str'},
        'service_package_activation_id': {'key': 'ServicePackageActivationId', 'type': 'str'},
        'code_package_name': {'key': 'CodePackageName', 'type': 'str'},
        'code_package_instance_id': {'key': 'CodePackageInstanceId', 'type': 'str'},
    }

    def __init__(self, service_manifest_name, code_package_name, code_package_instance_id, service_package_activation_id=None):
        super(RestartDeployedCodePackageDescription, self).__init__()
        self.service_manifest_name = service_manifest_name
        self.service_package_activation_id = service_package_activation_id
        self.code_package_name = code_package_name
        self.code_package_instance_id = code_package_instance_id
