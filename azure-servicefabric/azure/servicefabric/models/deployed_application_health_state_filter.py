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


class DeployedApplicationHealthStateFilter(Model):
    """Defines matching criteria to determine whether a deployed application
    should be included as a child of an application in the cluster health
    chunk.
    The deployed applications are only returned if the parent application
    matches a filter specified in the cluster health chunk query description.
    One filter can match zero, one or multiple deployed applications, depending
    on its properties.
    .

    :param node_name_filter: The name of the node where the application is
     deployed in order to match the filter.
     If specified, the filter is applied only to the application deployed on
     the specified node.
     If the application is not deployed on the node with the specified name, no
     deployed application is returned in the cluster health chunk based on this
     filter.
     Otherwise, the deployed application is included in the cluster health
     chunk if it respects the other filter properties.
     If not specified, all deployed applications that match the parent filters
     (if any) are taken into consideration and matched against the other filter
     members, like health state filter.
    :type node_name_filter: str
    :param health_state_filter: The filter for the health state of the
     deployed applications. It allows selecting deployed applications if they
     match the desired health states.
     The possible values are integer value of one of the following health
     states. Only deployed applications that match the filter are returned. All
     deployed applications are used to evaluate the cluster aggregated health
     state.
     If not specified, default value is None, unless the node name is
     specified. If the filter has default value and node name is specified, the
     matching deployed application is returned.
     The state values are flag based enumeration, so the value could be a
     combination of these values obtained using bitwise 'OR' operator.
     For example, if the provided value is 6, it matches deployed applications
     with HealthState value of OK (2) and Warning (4).
     - Default - Default value. Matches any HealthState. The value is zero.
     - None - Filter that doesn't match any HealthState value. Used in order to
     return no results on a given collection of states. The value is 1.
     - Ok - Filter that matches input with HealthState value Ok. The value is
     2.
     - Warning - Filter that matches input with HealthState value Warning. The
     value is 4.
     - Error - Filter that matches input with HealthState value Error. The
     value is 8.
     - All - Filter that matches input with any HealthState value. The value is
     65535.
     . Default value: 0 .
    :type health_state_filter: int
    :param deployed_service_package_filters: Defines a list of filters that
     specify which deployed service packages to be included in the returned
     cluster health chunk as children of the parent deployed application. The
     deployed service packages are returned only if the parent deployed
     application matches a filter.
     If the list is empty, no deployed service packages are returned. All the
     deployed service packages are used to evaluate the parent deployed
     application aggregated health state, regardless of the input filters.
     The deployed application filter may specify multiple deployed service
     package filters.
     For example, it can specify a filter to return all deployed service
     packages with health state Error and another filter to always include a
     deployed service package on a node.
    :type deployed_service_package_filters:
     list[~azure.servicefabric.models.DeployedServicePackageHealthStateFilter]
    """

    _attribute_map = {
        'node_name_filter': {'key': 'NodeNameFilter', 'type': 'str'},
        'health_state_filter': {'key': 'HealthStateFilter', 'type': 'int'},
        'deployed_service_package_filters': {'key': 'DeployedServicePackageFilters', 'type': '[DeployedServicePackageHealthStateFilter]'},
    }

    def __init__(self, node_name_filter=None, health_state_filter=0, deployed_service_package_filters=None):
        super(DeployedApplicationHealthStateFilter, self).__init__()
        self.node_name_filter = node_name_filter
        self.health_state_filter = health_state_filter
        self.deployed_service_package_filters = deployed_service_package_filters
