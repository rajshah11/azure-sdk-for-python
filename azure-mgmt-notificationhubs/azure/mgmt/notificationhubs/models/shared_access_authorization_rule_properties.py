# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SharedAccessAuthorizationRuleProperties(Model):
    """
    SharedAccessAuthorizationRule properties.

    :param str primary_key: The primary key that was used.
    :param str secondary_key: The secondary key that was used.
    :param str key_name: The name of the key that was used.
    :param str claim_type: The type of the claim.
    :param str claim_value: The value of the claim.
    :param list rights: The rights associated with the rule.
    :param datetime created_time: The time at which the authorization rule
     was created.
    :param datetime modified_time: The most recent time the rule was updated.
    :param int revision: The revision number for the rule.
    """

    _required = []

    _attribute_map = {
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'key_name': {'key': 'keyName', 'type': 'str'},
        'claim_type': {'key': 'claimType', 'type': 'str'},
        'claim_value': {'key': 'claimValue', 'type': 'str'},
        'rights': {'key': 'rights', 'type': '[AccessRights]'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'modified_time': {'key': 'modifiedTime', 'type': 'iso-8601'},
        'revision': {'key': 'revision', 'type': 'int'},
    }

    def __init__(self, primary_key=None, secondary_key=None, key_name=None, claim_type=None, claim_value=None, rights=None, created_time=None, modified_time=None, revision=None):
        self.primary_key = primary_key
        self.secondary_key = secondary_key
        self.key_name = key_name
        self.claim_type = claim_type
        self.claim_value = claim_value
        self.rights = rights
        self.created_time = created_time
        self.modified_time = modified_time
        self.revision = revision