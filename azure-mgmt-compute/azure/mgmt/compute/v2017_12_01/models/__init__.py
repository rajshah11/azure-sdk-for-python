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

from .instance_view_status import InstanceViewStatus
from .sub_resource import SubResource
from .sku import Sku
from .availability_set import AvailabilitySet
from .virtual_machine_size import VirtualMachineSize
from .virtual_machine_extension_image import VirtualMachineExtensionImage
from .virtual_machine_image_resource import VirtualMachineImageResource
from .virtual_machine_extension_instance_view import VirtualMachineExtensionInstanceView
from .virtual_machine_extension import VirtualMachineExtension
from .purchase_plan import PurchasePlan
from .os_disk_image import OSDiskImage
from .data_disk_image import DataDiskImage
from .virtual_machine_image import VirtualMachineImage
from .usage_name import UsageName
from .usage import Usage
from .virtual_machine_capture_parameters import VirtualMachineCaptureParameters
from .virtual_machine_capture_result import VirtualMachineCaptureResult
from .plan import Plan
from .hardware_profile import HardwareProfile
from .image_reference import ImageReference
from .key_vault_secret_reference import KeyVaultSecretReference
from .key_vault_key_reference import KeyVaultKeyReference
from .disk_encryption_settings import DiskEncryptionSettings
from .virtual_hard_disk import VirtualHardDisk
from .managed_disk_parameters import ManagedDiskParameters
from .os_disk import OSDisk
from .data_disk import DataDisk
from .storage_profile import StorageProfile
from .additional_unattend_content import AdditionalUnattendContent
from .win_rm_listener import WinRMListener
from .win_rm_configuration import WinRMConfiguration
from .windows_configuration import WindowsConfiguration
from .ssh_public_key import SshPublicKey
from .ssh_configuration import SshConfiguration
from .linux_configuration import LinuxConfiguration
from .vault_certificate import VaultCertificate
from .vault_secret_group import VaultSecretGroup
from .os_profile import OSProfile
from .network_interface_reference import NetworkInterfaceReference
from .network_profile import NetworkProfile
from .boot_diagnostics import BootDiagnostics
from .diagnostics_profile import DiagnosticsProfile
from .virtual_machine_extension_handler_instance_view import VirtualMachineExtensionHandlerInstanceView
from .virtual_machine_agent_instance_view import VirtualMachineAgentInstanceView
from .disk_instance_view import DiskInstanceView
from .boot_diagnostics_instance_view import BootDiagnosticsInstanceView
from .virtual_machine_identity import VirtualMachineIdentity
from .maintenance_redeploy_status import MaintenanceRedeployStatus
from .virtual_machine_instance_view import VirtualMachineInstanceView
from .virtual_machine import VirtualMachine
from .rolling_upgrade_policy import RollingUpgradePolicy
from .upgrade_policy import UpgradePolicy
from .image_os_disk import ImageOSDisk
from .image_data_disk import ImageDataDisk
from .image_storage_profile import ImageStorageProfile
from .image import Image
from .virtual_machine_scale_set_identity import VirtualMachineScaleSetIdentity
from .virtual_machine_scale_set_os_profile import VirtualMachineScaleSetOSProfile
from .virtual_machine_scale_set_update_os_profile import VirtualMachineScaleSetUpdateOSProfile
from .virtual_machine_scale_set_managed_disk_parameters import VirtualMachineScaleSetManagedDiskParameters
from .virtual_machine_scale_set_os_disk import VirtualMachineScaleSetOSDisk
from .virtual_machine_scale_set_update_os_disk import VirtualMachineScaleSetUpdateOSDisk
from .virtual_machine_scale_set_data_disk import VirtualMachineScaleSetDataDisk
from .virtual_machine_scale_set_storage_profile import VirtualMachineScaleSetStorageProfile
from .virtual_machine_scale_set_update_storage_profile import VirtualMachineScaleSetUpdateStorageProfile
from .api_entity_reference import ApiEntityReference
from .virtual_machine_scale_set_public_ip_address_configuration_dns_settings import VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
from .virtual_machine_scale_set_public_ip_address_configuration import VirtualMachineScaleSetPublicIPAddressConfiguration
from .virtual_machine_scale_set_update_public_ip_address_configuration import VirtualMachineScaleSetUpdatePublicIPAddressConfiguration
from .virtual_machine_scale_set_ip_configuration import VirtualMachineScaleSetIPConfiguration
from .virtual_machine_scale_set_update_ip_configuration import VirtualMachineScaleSetUpdateIPConfiguration
from .virtual_machine_scale_set_network_configuration_dns_settings import VirtualMachineScaleSetNetworkConfigurationDnsSettings
from .virtual_machine_scale_set_network_configuration import VirtualMachineScaleSetNetworkConfiguration
from .virtual_machine_scale_set_update_network_configuration import VirtualMachineScaleSetUpdateNetworkConfiguration
from .virtual_machine_scale_set_network_profile import VirtualMachineScaleSetNetworkProfile
from .virtual_machine_scale_set_update_network_profile import VirtualMachineScaleSetUpdateNetworkProfile
from .virtual_machine_scale_set_extension import VirtualMachineScaleSetExtension
from .virtual_machine_scale_set_extension_profile import VirtualMachineScaleSetExtensionProfile
from .virtual_machine_scale_set_vm_profile import VirtualMachineScaleSetVMProfile
from .virtual_machine_scale_set_update_vm_profile import VirtualMachineScaleSetUpdateVMProfile
from .virtual_machine_scale_set import VirtualMachineScaleSet
from .virtual_machine_scale_set_update import VirtualMachineScaleSetUpdate
from .virtual_machine_scale_set_vm_instance_ids import VirtualMachineScaleSetVMInstanceIDs
from .virtual_machine_scale_set_vm_instance_required_ids import VirtualMachineScaleSetVMInstanceRequiredIDs
from .virtual_machine_status_code_count import VirtualMachineStatusCodeCount
from .virtual_machine_scale_set_instance_view_statuses_summary import VirtualMachineScaleSetInstanceViewStatusesSummary
from .virtual_machine_scale_set_vm_extensions_summary import VirtualMachineScaleSetVMExtensionsSummary
from .virtual_machine_scale_set_instance_view import VirtualMachineScaleSetInstanceView
from .virtual_machine_scale_set_sku_capacity import VirtualMachineScaleSetSkuCapacity
from .virtual_machine_scale_set_sku import VirtualMachineScaleSetSku
from .virtual_machine_scale_set_vm import VirtualMachineScaleSetVM
from .virtual_machine_health_status import VirtualMachineHealthStatus
from .virtual_machine_scale_set_vm_instance_view import VirtualMachineScaleSetVMInstanceView
from .rolling_upgrade_running_status import RollingUpgradeRunningStatus
from .rolling_upgrade_progress_info import RollingUpgradeProgressInfo
from .api_error_base import ApiErrorBase
from .inner_error import InnerError
from .api_error import ApiError
from .rolling_upgrade_status_info import RollingUpgradeStatusInfo
from .compute_long_running_operation_properties import ComputeLongRunningOperationProperties
from .resource import Resource
from .update_resource import UpdateResource
from .sub_resource_read_only import SubResourceReadOnly
from .recovery_walk_response import RecoveryWalkResponse
from .operation_status_response import OperationStatusResponse
from .request_rate_by_interval_input import RequestRateByIntervalInput
from .throttled_requests_input import ThrottledRequestsInput
from .log_analytics_input_base import LogAnalyticsInputBase
from .log_analytics_output import LogAnalyticsOutput
from .log_analytics_operation_result import LogAnalyticsOperationResult
from .run_command_input_parameter import RunCommandInputParameter
from .run_command_input import RunCommandInput
from .run_command_parameter_definition import RunCommandParameterDefinition
from .run_command_document_base import RunCommandDocumentBase
from .run_command_document import RunCommandDocument
from .run_command_result import RunCommandResult
from .availability_set_paged import AvailabilitySetPaged
from .virtual_machine_size_paged import VirtualMachineSizePaged
from .usage_paged import UsagePaged
from .image_paged import ImagePaged
from .virtual_machine_paged import VirtualMachinePaged
from .virtual_machine_scale_set_paged import VirtualMachineScaleSetPaged
from .virtual_machine_scale_set_sku_paged import VirtualMachineScaleSetSkuPaged
from .virtual_machine_scale_set_extension_paged import VirtualMachineScaleSetExtensionPaged
from .virtual_machine_scale_set_vm_paged import VirtualMachineScaleSetVMPaged
from .run_command_document_base_paged import RunCommandDocumentBasePaged
from .compute_management_client_enums import (
    StatusLevelTypes,
    OperatingSystemTypes,
    VirtualMachineSizeTypes,
    CachingTypes,
    DiskCreateOptionTypes,
    StorageAccountTypes,
    PassNames,
    ComponentNames,
    SettingNames,
    ProtocolTypes,
    ResourceIdentityType,
    MaintenanceOperationResultCodeTypes,
    UpgradeMode,
    OperatingSystemStateTypes,
    IPVersion,
    VirtualMachinePriorityTypes,
    VirtualMachineScaleSetSkuScaleType,
    RollingUpgradeStatusCode,
    RollingUpgradeActionType,
    IntervalInMins,
    InstanceViewTypes,
)

__all__ = [
    'InstanceViewStatus',
    'SubResource',
    'Sku',
    'AvailabilitySet',
    'VirtualMachineSize',
    'VirtualMachineExtensionImage',
    'VirtualMachineImageResource',
    'VirtualMachineExtensionInstanceView',
    'VirtualMachineExtension',
    'PurchasePlan',
    'OSDiskImage',
    'DataDiskImage',
    'VirtualMachineImage',
    'UsageName',
    'Usage',
    'VirtualMachineCaptureParameters',
    'VirtualMachineCaptureResult',
    'Plan',
    'HardwareProfile',
    'ImageReference',
    'KeyVaultSecretReference',
    'KeyVaultKeyReference',
    'DiskEncryptionSettings',
    'VirtualHardDisk',
    'ManagedDiskParameters',
    'OSDisk',
    'DataDisk',
    'StorageProfile',
    'AdditionalUnattendContent',
    'WinRMListener',
    'WinRMConfiguration',
    'WindowsConfiguration',
    'SshPublicKey',
    'SshConfiguration',
    'LinuxConfiguration',
    'VaultCertificate',
    'VaultSecretGroup',
    'OSProfile',
    'NetworkInterfaceReference',
    'NetworkProfile',
    'BootDiagnostics',
    'DiagnosticsProfile',
    'VirtualMachineExtensionHandlerInstanceView',
    'VirtualMachineAgentInstanceView',
    'DiskInstanceView',
    'BootDiagnosticsInstanceView',
    'VirtualMachineIdentity',
    'MaintenanceRedeployStatus',
    'VirtualMachineInstanceView',
    'VirtualMachine',
    'RollingUpgradePolicy',
    'UpgradePolicy',
    'ImageOSDisk',
    'ImageDataDisk',
    'ImageStorageProfile',
    'Image',
    'VirtualMachineScaleSetIdentity',
    'VirtualMachineScaleSetOSProfile',
    'VirtualMachineScaleSetUpdateOSProfile',
    'VirtualMachineScaleSetManagedDiskParameters',
    'VirtualMachineScaleSetOSDisk',
    'VirtualMachineScaleSetUpdateOSDisk',
    'VirtualMachineScaleSetDataDisk',
    'VirtualMachineScaleSetStorageProfile',
    'VirtualMachineScaleSetUpdateStorageProfile',
    'ApiEntityReference',
    'VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings',
    'VirtualMachineScaleSetPublicIPAddressConfiguration',
    'VirtualMachineScaleSetUpdatePublicIPAddressConfiguration',
    'VirtualMachineScaleSetIPConfiguration',
    'VirtualMachineScaleSetUpdateIPConfiguration',
    'VirtualMachineScaleSetNetworkConfigurationDnsSettings',
    'VirtualMachineScaleSetNetworkConfiguration',
    'VirtualMachineScaleSetUpdateNetworkConfiguration',
    'VirtualMachineScaleSetNetworkProfile',
    'VirtualMachineScaleSetUpdateNetworkProfile',
    'VirtualMachineScaleSetExtension',
    'VirtualMachineScaleSetExtensionProfile',
    'VirtualMachineScaleSetVMProfile',
    'VirtualMachineScaleSetUpdateVMProfile',
    'VirtualMachineScaleSet',
    'VirtualMachineScaleSetUpdate',
    'VirtualMachineScaleSetVMInstanceIDs',
    'VirtualMachineScaleSetVMInstanceRequiredIDs',
    'VirtualMachineStatusCodeCount',
    'VirtualMachineScaleSetInstanceViewStatusesSummary',
    'VirtualMachineScaleSetVMExtensionsSummary',
    'VirtualMachineScaleSetInstanceView',
    'VirtualMachineScaleSetSkuCapacity',
    'VirtualMachineScaleSetSku',
    'VirtualMachineScaleSetVM',
    'VirtualMachineHealthStatus',
    'VirtualMachineScaleSetVMInstanceView',
    'RollingUpgradeRunningStatus',
    'RollingUpgradeProgressInfo',
    'ApiErrorBase',
    'InnerError',
    'ApiError',
    'RollingUpgradeStatusInfo',
    'ComputeLongRunningOperationProperties',
    'Resource',
    'UpdateResource',
    'SubResourceReadOnly',
    'RecoveryWalkResponse',
    'OperationStatusResponse',
    'RequestRateByIntervalInput',
    'ThrottledRequestsInput',
    'LogAnalyticsInputBase',
    'LogAnalyticsOutput',
    'LogAnalyticsOperationResult',
    'RunCommandInputParameter',
    'RunCommandInput',
    'RunCommandParameterDefinition',
    'RunCommandDocumentBase',
    'RunCommandDocument',
    'RunCommandResult',
    'AvailabilitySetPaged',
    'VirtualMachineSizePaged',
    'UsagePaged',
    'ImagePaged',
    'VirtualMachinePaged',
    'VirtualMachineScaleSetPaged',
    'VirtualMachineScaleSetSkuPaged',
    'VirtualMachineScaleSetExtensionPaged',
    'VirtualMachineScaleSetVMPaged',
    'RunCommandDocumentBasePaged',
    'StatusLevelTypes',
    'OperatingSystemTypes',
    'VirtualMachineSizeTypes',
    'CachingTypes',
    'DiskCreateOptionTypes',
    'StorageAccountTypes',
    'PassNames',
    'ComponentNames',
    'SettingNames',
    'ProtocolTypes',
    'ResourceIdentityType',
    'MaintenanceOperationResultCodeTypes',
    'UpgradeMode',
    'OperatingSystemStateTypes',
    'IPVersion',
    'VirtualMachinePriorityTypes',
    'VirtualMachineScaleSetSkuScaleType',
    'RollingUpgradeStatusCode',
    'RollingUpgradeActionType',
    'IntervalInMins',
    'InstanceViewTypes',
]
