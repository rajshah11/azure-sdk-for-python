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


class JobSchedule(Model):
    """Definition of the job schedule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Gets the id of the resource.
    :vartype id: str
    :ivar name: Gets the name of the variable.
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param job_schedule_id: Gets or sets the id of job schedule.
    :type job_schedule_id: str
    :param schedule: Gets or sets the schedule.
    :type schedule: ~azure.mgmt.automation.models.ScheduleAssociationProperty
    :param runbook: Gets or sets the runbook.
    :type runbook: ~azure.mgmt.automation.models.RunbookAssociationProperty
    :param run_on: Gets or sets the hybrid worker group that the scheduled job
     should run on.
    :type run_on: str
    :param parameters: Gets or sets the parameters of the job schedule.
    :type parameters: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'job_schedule_id': {'key': 'properties.jobScheduleId', 'type': 'str'},
        'schedule': {'key': 'properties.schedule', 'type': 'ScheduleAssociationProperty'},
        'runbook': {'key': 'properties.runbook', 'type': 'RunbookAssociationProperty'},
        'run_on': {'key': 'properties.runOn', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': '{str}'},
    }

    def __init__(self, job_schedule_id=None, schedule=None, runbook=None, run_on=None, parameters=None):
        super(JobSchedule, self).__init__()
        self.id = None
        self.name = None
        self.type = None
        self.job_schedule_id = job_schedule_id
        self.schedule = schedule
        self.runbook = runbook
        self.run_on = run_on
        self.parameters = parameters
