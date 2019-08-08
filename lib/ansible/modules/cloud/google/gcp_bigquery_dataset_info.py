#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_bigquery_dataset_info
description:
- Gather info for GCP Dataset
- This module was called C(gcp_bigquery_dataset_facts) before Ansible 2.9. The usage
  has not changed.
short_description: Gather info for GCP Dataset
version_added: 2.8
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options: {}
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: get info on a dataset
  gcp_bigquery_dataset_info:
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    name:
      description:
      - Dataset name.
      returned: success
      type: str
    access:
      description:
      - Access controls on the bucket.
      returned: success
      type: complex
      contains:
        domain:
          description:
          - A domain to grant access to. Any users signed in with the domain specified
            will be granted the specified access .
          returned: success
          type: str
        groupByEmail:
          description:
          - An email address of a Google Group to grant access to.
          returned: success
          type: str
        role:
          description:
          - Describes the rights granted to the user specified by the other member
            of the access object .
          returned: success
          type: str
        specialGroup:
          description:
          - A special group to grant access to.
          returned: success
          type: str
        userByEmail:
          description:
          - 'An email address of a user to grant access to. For example: fred@example.com
            .'
          returned: success
          type: str
        view:
          description:
          - A view from a different dataset to grant access to. Queries executed against
            that view will have read access to tables in this dataset. The role field
            is not required when this field is set. If that view is updated by any
            user, access to the view needs to be granted again via an update operation.
          returned: success
          type: complex
          contains:
            datasetId:
              description:
              - The ID of the dataset containing this table.
              returned: success
              type: str
            projectId:
              description:
              - The ID of the project containing this table.
              returned: success
              type: str
            tableId:
              description:
              - The ID of the table. The ID must contain only letters (a-z, A-Z),
                numbers (0-9), or underscores. The maximum length is 1,024 characters.
              returned: success
              type: str
    creationTime:
      description:
      - The time when this dataset was created, in milliseconds since the epoch.
      returned: success
      type: int
    datasetReference:
      description:
      - A reference that identifies the dataset.
      returned: success
      type: complex
      contains:
        datasetId:
          description:
          - A unique ID for this dataset, without the project name. The ID must contain
            only letters (a-z, A-Z), numbers (0-9), or underscores. The maximum length
            is 1,024 characters.
          returned: success
          type: str
        projectId:
          description:
          - The ID of the project containing this dataset.
          returned: success
          type: str
    defaultTableExpirationMs:
      description:
      - The default lifetime of all tables in the dataset, in milliseconds .
      returned: success
      type: int
    description:
      description:
      - A user-friendly description of the dataset.
      returned: success
      type: str
    friendlyName:
      description:
      - A descriptive name for the dataset.
      returned: success
      type: str
    id:
      description:
      - The fully-qualified unique name of the dataset in the format projectId:datasetId.
        The dataset name without the project name is given in the datasetId field
        .
      returned: success
      type: str
    labels:
      description:
      - The labels associated with this dataset. You can use these to organize and
        group your datasets .
      returned: success
      type: dict
    lastModifiedTime:
      description:
      - The date when this dataset or any of its tables was last modified, in milliseconds
        since the epoch.
      returned: success
      type: int
    location:
      description:
      - The geographic location where the dataset should reside. Possible values include
        EU and US. The default value is US.
      returned: success
      type: str
'''

################################################################################
# Imports
################################################################################
from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict())

    if module._name == 'gcp_bigquery_dataset_facts':
        module.deprecate("The 'gcp_bigquery_dataset_facts' module has been renamed to 'gcp_bigquery_dataset_info'", version='2.13')

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/bigquery']

    items = fetch_list(module, collection(module))
    if items.get('datasets'):
        items = items.get('datasets')
    else:
        items = []
    return_value = {'resources': items}
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/bigquery/v2/projects/{project}/datasets".format(**module.params)


def fetch_list(module, link):
    auth = GcpSession(module, 'bigquery')
    response = auth.get(link)
    return return_if_object(module, response)


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
