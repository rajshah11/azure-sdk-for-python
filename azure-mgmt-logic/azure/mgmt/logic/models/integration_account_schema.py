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


class IntegrationAccountSchema(Resource):
    """The integration account schema.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource id.
    :vartype id: str
    :ivar name: Gets the resource name.
    :vartype name: str
    :ivar type: Gets the resource type.
    :vartype type: str
    :param location: The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param schema_type: The schema type. Possible values include:
     'NotSpecified', 'Xml'
    :type schema_type: str or ~azure.mgmt.logic.models.SchemaType
    :param target_namespace: The target namespace of the schema.
    :type target_namespace: str
    :param document_name: The document name.
    :type document_name: str
    :param file_name: The file name.
    :type file_name: str
    :ivar created_time: The created time.
    :vartype created_time: datetime
    :ivar changed_time: The changed time.
    :vartype changed_time: datetime
    :param metadata: The metadata.
    :type metadata: object
    :param content: The content.
    :type content: str
    :param content_type: The content type.
    :type content_type: str
    :ivar content_link: The content link.
    :vartype content_link: ~azure.mgmt.logic.models.ContentLink
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'schema_type': {'required': True},
        'created_time': {'readonly': True},
        'changed_time': {'readonly': True},
        'content_link': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'schema_type': {'key': 'properties.schemaType', 'type': 'SchemaType'},
        'target_namespace': {'key': 'properties.targetNamespace', 'type': 'str'},
        'document_name': {'key': 'properties.documentName', 'type': 'str'},
        'file_name': {'key': 'properties.fileName', 'type': 'str'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'changed_time': {'key': 'properties.changedTime', 'type': 'iso-8601'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'content': {'key': 'properties.content', 'type': 'str'},
        'content_type': {'key': 'properties.contentType', 'type': 'str'},
        'content_link': {'key': 'properties.contentLink', 'type': 'ContentLink'},
    }

    def __init__(self, schema_type, location=None, tags=None, target_namespace=None, document_name=None, file_name=None, metadata=None, content=None, content_type=None):
        super(IntegrationAccountSchema, self).__init__(location=location, tags=tags)
        self.schema_type = schema_type
        self.target_namespace = target_namespace
        self.document_name = document_name
        self.file_name = file_name
        self.created_time = None
        self.changed_time = None
        self.metadata = metadata
        self.content = content
        self.content_type = content_type
        self.content_link = None
