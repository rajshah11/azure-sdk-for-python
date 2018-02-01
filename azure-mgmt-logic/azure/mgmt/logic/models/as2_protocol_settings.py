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


class AS2ProtocolSettings(Model):
    """The AS2 agreement protocol settings.

    :param message_connection_settings: The message connection settings.
    :type message_connection_settings:
     ~azure.mgmt.logic.models.AS2MessageConnectionSettings
    :param acknowledgement_connection_settings: The acknowledgement connection
     settings.
    :type acknowledgement_connection_settings:
     ~azure.mgmt.logic.models.AS2AcknowledgementConnectionSettings
    :param mdn_settings: The MDN settings.
    :type mdn_settings: ~azure.mgmt.logic.models.AS2MdnSettings
    :param security_settings: The security settings.
    :type security_settings: ~azure.mgmt.logic.models.AS2SecuritySettings
    :param validation_settings: The validation settings.
    :type validation_settings: ~azure.mgmt.logic.models.AS2ValidationSettings
    :param envelope_settings: The envelope settings.
    :type envelope_settings: ~azure.mgmt.logic.models.AS2EnvelopeSettings
    :param error_settings: The error settings.
    :type error_settings: ~azure.mgmt.logic.models.AS2ErrorSettings
    """

    _validation = {
        'message_connection_settings': {'required': True},
        'acknowledgement_connection_settings': {'required': True},
        'mdn_settings': {'required': True},
        'security_settings': {'required': True},
        'validation_settings': {'required': True},
        'envelope_settings': {'required': True},
        'error_settings': {'required': True},
    }

    _attribute_map = {
        'message_connection_settings': {'key': 'messageConnectionSettings', 'type': 'AS2MessageConnectionSettings'},
        'acknowledgement_connection_settings': {'key': 'acknowledgementConnectionSettings', 'type': 'AS2AcknowledgementConnectionSettings'},
        'mdn_settings': {'key': 'mdnSettings', 'type': 'AS2MdnSettings'},
        'security_settings': {'key': 'securitySettings', 'type': 'AS2SecuritySettings'},
        'validation_settings': {'key': 'validationSettings', 'type': 'AS2ValidationSettings'},
        'envelope_settings': {'key': 'envelopeSettings', 'type': 'AS2EnvelopeSettings'},
        'error_settings': {'key': 'errorSettings', 'type': 'AS2ErrorSettings'},
    }

    def __init__(self, message_connection_settings, acknowledgement_connection_settings, mdn_settings, security_settings, validation_settings, envelope_settings, error_settings):
        super(AS2ProtocolSettings, self).__init__()
        self.message_connection_settings = message_connection_settings
        self.acknowledgement_connection_settings = acknowledgement_connection_settings
        self.mdn_settings = mdn_settings
        self.security_settings = security_settings
        self.validation_settings = validation_settings
        self.envelope_settings = envelope_settings
        self.error_settings = error_settings
