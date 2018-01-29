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

from .proxy_only_resource import ProxyOnlyResource


class BackupRequest(ProxyOnlyResource):
    """Description of a backup which will be performed.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param backup_request_name: Name of the backup.
    :type backup_request_name: str
    :param enabled: True if the backup schedule is enabled (must be included
     in that case), false if the backup schedule should be disabled.
    :type enabled: bool
    :param storage_account_url: SAS URL to the container.
    :type storage_account_url: str
    :param backup_schedule: Schedule for the backup if it is executed
     periodically.
    :type backup_schedule: ~azure.mgmt.web.models.BackupSchedule
    :param databases: Databases included in the backup.
    :type databases: list[~azure.mgmt.web.models.DatabaseBackupSetting]
    :param backup_request_type: Type of the backup. Possible values include:
     'Default', 'Clone', 'Relocation', 'Snapshot'
    :type backup_request_type: str or
     ~azure.mgmt.web.models.BackupRestoreOperationType
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'backup_request_name': {'required': True},
        'storage_account_url': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'backup_request_name': {'key': 'properties.name', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'storage_account_url': {'key': 'properties.storageAccountUrl', 'type': 'str'},
        'backup_schedule': {'key': 'properties.backupSchedule', 'type': 'BackupSchedule'},
        'databases': {'key': 'properties.databases', 'type': '[DatabaseBackupSetting]'},
        'backup_request_type': {'key': 'properties.type', 'type': 'BackupRestoreOperationType'},
    }

    def __init__(self, backup_request_name, storage_account_url, kind=None, enabled=None, backup_schedule=None, databases=None, backup_request_type=None):
        super(BackupRequest, self).__init__(kind=kind)
        self.backup_request_name = backup_request_name
        self.enabled = enabled
        self.storage_account_url = storage_account_url
        self.backup_schedule = backup_schedule
        self.databases = databases
        self.backup_request_type = backup_request_type
