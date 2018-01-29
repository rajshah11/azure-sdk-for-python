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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class CertificatesOperations(object):
    """CertificatesOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    :ivar api_version: The version of the API. Constant value: "2017-07-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2017-07-01"

        self.config = config

    def list_by_iot_hub(
            self, resource_group_name, resource_name, custom_headers=None, raw=False, **operation_config):
        """Get the certificate list.

        Returns the list of certificates.

        :param resource_group_name: The name of the resource group that
         contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CertificateListDescription or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.iothub.models.CertificateListDescription or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothub.models.ErrorDetailsException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CertificateListDescription', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get(
            self, resource_group_name, resource_name, certificate_name, custom_headers=None, raw=False, **operation_config):
        """Get the certificate.

        Returns the certificate.

        :param resource_group_name: The name of the resource group that
         contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param certificate_name: The name of the certificate
        :type certificate_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CertificateDescription or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.iothub.models.CertificateDescription or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothub.models.ErrorDetailsException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str', pattern=r'^[A-Za-z0-9-._]{1,64}$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CertificateDescription', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_or_update(
            self, resource_group_name, resource_name, certificate_name, if_match=None, certificate=None, custom_headers=None, raw=False, **operation_config):
        """Upload the certificate to the IoT hub.

        Adds new or replaces existing certificate.

        :param resource_group_name: The name of the resource group that
         contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param certificate_name: The name of the certificate
        :type certificate_name: str
        :param if_match: ETag of the Certificate. Do not specify for creating
         a brand new certificate. Required to update an existing certificate.
        :type if_match: str
        :param certificate: base-64 representation of the X509 leaf
         certificate .cer file or just .pem file content.
        :type certificate: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CertificateDescription or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.iothub.models.CertificateDescription or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothub.models.ErrorDetailsException>`
        """
        certificate_description = models.CertificateBodyDescription(certificate=certificate)

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str', pattern=r'^[A-Za-z0-9-._]{1,64}$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(certificate_description, 'CertificateBodyDescription')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CertificateDescription', response)
        if response.status_code == 201:
            deserialized = self._deserialize('CertificateDescription', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete(
            self, resource_group_name, resource_name, certificate_name, if_match, custom_headers=None, raw=False, **operation_config):
        """Delete an X509 certificate.

        Deletes an existing X509 certificate or does nothing if it does not
        exist.

        :param resource_group_name: The name of the resource group that
         contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param certificate_name: The name of the certificate
        :type certificate_name: str
        :param if_match: ETag of the Certificate.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothub.models.ErrorDetailsException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str', pattern=r'^[A-Za-z0-9-._]{1,64}$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorDetailsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def generate_verification_code(
            self, resource_group_name, resource_name, certificate_name, if_match, custom_headers=None, raw=False, **operation_config):
        """Generate verification code for proof of possession flow.

        Generates verification code for proof of possession flow. The
        verification code will be used to generate a leaf certificate.

        :param resource_group_name: The name of the resource group that
         contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param certificate_name: The name of the certificate
        :type certificate_name: str
        :param if_match: ETag of the Certificate.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CertificateWithNonceDescription or ClientRawResponse if
         raw=true
        :rtype: ~azure.mgmt.iothub.models.CertificateWithNonceDescription or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothub.models.ErrorDetailsException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/generateVerificationCode'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str', pattern=r'^[A-Za-z0-9-._]{1,64}$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CertificateWithNonceDescription', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def verify(
            self, resource_group_name, resource_name, certificate_name, if_match, certificate=None, custom_headers=None, raw=False, **operation_config):
        """Verify certificate's private key possession.

        Verifies the certificate's private key possession by providing the leaf
        cert issued by the verifying pre uploaded certificate.

        :param resource_group_name: The name of the resource group that
         contains the IoT hub.
        :type resource_group_name: str
        :param resource_name: The name of the IoT hub.
        :type resource_name: str
        :param certificate_name: The name of the certificate
        :type certificate_name: str
        :param if_match: ETag of the Certificate.
        :type if_match: str
        :param certificate: base-64 representation of X509 certificate .cer
         file or just .pem file content.
        :type certificate: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CertificateDescription or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.iothub.models.CertificateDescription or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDetailsException<azure.mgmt.iothub.models.ErrorDetailsException>`
        """
        certificate_verification_body = models.CertificateVerificationDescription(certificate=certificate)

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/verify'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str', pattern=r'^[A-Za-z0-9-._]{1,64}$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(certificate_verification_body, 'CertificateVerificationDescription')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorDetailsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CertificateDescription', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
