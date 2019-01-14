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
module: gcp_spanner_database
description:
- A Cloud Spanner Database which is hosted on a Spanner instance.
short_description: Creates a GCP Database
version_added: 2.7
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
  name:
    description:
    - A unique identifier for the database, which cannot be changed after the instance
      is created. Values are of the form projects/<project>/instances/[a-z][-a-z0-9]*[a-z0-9].
      The final segment of the name must be between 6 and 30 characters in length.
    required: false
  extra_statements:
    description:
    - 'An optional list of DDL statements to run inside the newly created database.
      Statements can create tables, indexes, etc. These statements execute atomically
      with the creation of the database: if there is an error in any statement, the
      database is not created.'
    required: false
  instance:
    description:
    - The instance to create the database on.
    - 'This field represents a link to a Instance resource in GCP. It can be specified
      in two ways. First, you can place in the name of the resource here as a string
      Alternatively, you can add `register: name-of-resource` to a gcp_spanner_instance
      task and then set this instance field to "{{ name-of-resource }}"'
    required: true
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: create a instance
  gcp_spanner_instance:
      name: "instance-database"
      display_name: My Spanner Instance
      node_count: 2
      labels:
        cost_center: ti-1700004
      config: regional-us-central1
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: instance

- name: create a database
  gcp_spanner_database:
      name: webstore
      instance: "{{ instance }}"
      project: "test_project"
      auth_kind: "serviceaccount"
      service_account_file: "/tmp/auth.pem"
      state: present
'''

RETURN = '''
name:
  description:
  - A unique identifier for the database, which cannot be changed after the instance
    is created. Values are of the form projects/<project>/instances/[a-z][-a-z0-9]*[a-z0-9].
    The final segment of the name must be between 6 and 30 characters in length.
  returned: success
  type: str
extraStatements:
  description:
  - 'An optional list of DDL statements to run inside the newly created database.
    Statements can create tables, indexes, etc. These statements execute atomically
    with the creation of the database: if there is an error in any statement, the
    database is not created.'
  returned: success
  type: list
instance:
  description:
  - The instance to create the database on.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(type='str'),
            extra_statements=dict(type='list', elements='str'),
            instance=dict(required=True),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/spanner.admin']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module))
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'spanner')
    return return_if_object(module, auth.post(link, resource_to_request(module)))


def update(module, link):
    auth = GcpSession(module, 'spanner')
    return return_if_object(module, auth.put(link, resource_to_request(module)))


def delete(module, link):
    auth = GcpSession(module, 'spanner')
    return return_if_object(module, auth.delete(link))


def resource_to_request(module):
    request = {u'name': module.params.get('name'), u'extraStatements': module.params.get('extra_statements')}
    request = encode_request(request, module)
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'spanner')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    res = {'project': module.params['project'], 'instance': replace_resource_dict(module.params['instance'], 'name'), 'name': module.params['name']}
    return "https://spanner.googleapis.com/v1/projects/{project}/instances/{instance}/databases/{name}".format(**res)


def collection(module):
    res = {'project': module.params['project'], 'instance': replace_resource_dict(module.params['instance'], 'name')}
    return "https://spanner.googleapis.com/v1/projects/{project}/instances/{instance}/databases".format(**res)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    result = decode_response(result, module)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)
    request = decode_response(request, module)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {u'name': response.get(u'name'), u'extraStatements': module.params.get('extra_statements')}


def decode_response(response, module):
    if not response:
        return response

    if 'name' not in response:
        return response

    if '/operations/' in response['name']:
        return response

    response['name'] = response['name'].split('/')[-1]
    return response


def encode_request(request, module):
    request['create_statement'] = "CREATE DATABASE `{0}`".format(module.params['name'])
    del request['name']
    return request


if __name__ == '__main__':
    main()
