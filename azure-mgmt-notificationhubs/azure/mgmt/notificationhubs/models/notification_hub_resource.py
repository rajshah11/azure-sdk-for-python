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

from .resource import Resource


class NotificationHubResource(Resource):
    """Description of a NotificationHub Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku: The sku of the created namespace
    :type sku: ~azure.mgmt.notificationhubs.models.Sku
    :param notification_hub_resource_name: The NotificationHub name.
    :type notification_hub_resource_name: str
    :param registration_ttl: The RegistrationTtl of the created
     NotificationHub
    :type registration_ttl: str
    :param authorization_rules: The AuthorizationRules of the created
     NotificationHub
    :type authorization_rules:
     list[~azure.mgmt.notificationhubs.models.SharedAccessAuthorizationRuleProperties]
    :param apns_credential: The ApnsCredential of the created NotificationHub
    :type apns_credential: ~azure.mgmt.notificationhubs.models.ApnsCredential
    :param wns_credential: The WnsCredential of the created NotificationHub
    :type wns_credential: ~azure.mgmt.notificationhubs.models.WnsCredential
    :param gcm_credential: The GcmCredential of the created NotificationHub
    :type gcm_credential: ~azure.mgmt.notificationhubs.models.GcmCredential
    :param mpns_credential: The MpnsCredential of the created NotificationHub
    :type mpns_credential: ~azure.mgmt.notificationhubs.models.MpnsCredential
    :param adm_credential: The AdmCredential of the created NotificationHub
    :type adm_credential: ~azure.mgmt.notificationhubs.models.AdmCredential
    :param baidu_credential: The BaiduCredential of the created
     NotificationHub
    :type baidu_credential:
     ~azure.mgmt.notificationhubs.models.BaiduCredential
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'notification_hub_resource_name': {'key': 'properties.name', 'type': 'str'},
        'registration_ttl': {'key': 'properties.registrationTtl', 'type': 'str'},
        'authorization_rules': {'key': 'properties.authorizationRules', 'type': '[SharedAccessAuthorizationRuleProperties]'},
        'apns_credential': {'key': 'properties.apnsCredential', 'type': 'ApnsCredential'},
        'wns_credential': {'key': 'properties.wnsCredential', 'type': 'WnsCredential'},
        'gcm_credential': {'key': 'properties.gcmCredential', 'type': 'GcmCredential'},
        'mpns_credential': {'key': 'properties.mpnsCredential', 'type': 'MpnsCredential'},
        'adm_credential': {'key': 'properties.admCredential', 'type': 'AdmCredential'},
        'baidu_credential': {'key': 'properties.baiduCredential', 'type': 'BaiduCredential'},
    }

    def __init__(self, location, tags=None, sku=None, notification_hub_resource_name=None, registration_ttl=None, authorization_rules=None, apns_credential=None, wns_credential=None, gcm_credential=None, mpns_credential=None, adm_credential=None, baidu_credential=None):
        super(NotificationHubResource, self).__init__(location=location, tags=tags, sku=sku)
        self.notification_hub_resource_name = notification_hub_resource_name
        self.registration_ttl = registration_ttl
        self.authorization_rules = authorization_rules
        self.apns_credential = apns_credential
        self.wns_credential = wns_credential
        self.gcm_credential = gcm_credential
        self.mpns_credential = mpns_credential
        self.adm_credential = adm_credential
        self.baidu_credential = baidu_credential
