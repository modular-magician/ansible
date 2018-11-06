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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ["preview"],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_target_pool
description:
- Represents a TargetPool resource, used for Load Balancing.
short_description: Creates a GCP TargetPool
version_added: 2.6
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
  backup_pool:
    description:
    - This field is applicable only when the containing target pool is serving a forwarding
      rule as the primary pool, and its failoverRatio field is properly set to a value
      between [0, 1].
    - 'backupPool and failoverRatio together define the fallback behavior of the primary
      target pool: if the ratio of the healthy instances in the primary pool is at
      or below failoverRatio, traffic arriving at the load-balanced IP will be directed
      to the backup pool.'
    - In case where failoverRatio and backupPool are not set, or all the instances
      in the backup pool are unhealthy, the traffic will be directed back to the primary
      pool in the "force" mode, where traffic will be spread to the healthy instances
      with the best effort, or to all instances when no instance is healthy.
    - 'This field represents a link to a TargetPool resource in GCP. It can be specified
      in two ways. You can add `register: name-of-resource` to a gcp_compute_target_pool
      task and then set this backup_pool field to "{{ name-of-resource }}" Alternatively,
      you can set this backup_pool to a dictionary with the selfLink key where the
      value is the selfLink of your TargetPool'
    required: false
  description:
    description:
    - An optional description of this resource.
    required: false
  failover_ratio:
    description:
    - This field is applicable only when the containing target pool is serving a forwarding
      rule as the primary pool (i.e., not as a backup pool to some other target pool).
      The value of the field must be in [0, 1].
    - 'If set, backupPool must also be set. They together define the fallback behavior
      of the primary target pool: if the ratio of the healthy instances in the primary
      pool is at or below this number, traffic arriving at the load-balanced IP will
      be directed to the backup pool.'
    - In case where failoverRatio is not set or all the instances in the backup pool
      are unhealthy, the traffic will be directed back to the primary pool in the
      "force" mode, where traffic will be spread to the healthy instances with the
      best effort, or to all instances when no instance is healthy.
    required: false
  health_check:
    description:
    - A reference to a HttpHealthCheck resource.
    - A member instance in this pool is considered healthy if and only if the health
      checks pass. If not specified it means all member instances will be considered
      healthy at all times.
    - 'This field represents a link to a HttpHealthCheck resource in GCP. It can be
      specified in two ways. You can add `register: name-of-resource` to a gcp_compute_http_health_check
      task and then set this health_check field to "{{ name-of-resource }}" Alternatively,
      you can set this health_check to a dictionary with the selfLink key where the
      value is the selfLink of your HttpHealthCheck'
    required: false
  instances:
    description:
    - A list of virtual machine instances serving this pool.
    - They must live in zones contained in the same region as this pool.
    required: false
  name:
    description:
    - Name of the resource. Provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
  session_affinity:
    description:
    - 'Session affinity option. Must be one of these values: - NONE: Connections from
      the same client IP may go to any instance in the pool.'
    - "- CLIENT_IP: Connections from the same client IP will go to the same instance
      in the pool while that instance remains healthy."
    - "- CLIENT_IP_PROTO: Connections from the same client IP with the same IP protocol
      will go to the same instance in the pool while that instance remains healthy."
    required: false
    choices:
    - NONE
    - CLIENT_IP
    - CLIENT_IP_PROTO
  region:
    description:
    - The region where the target pool resides.
    required: true
extends_documentation_fragment: gcp
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/rest/v1/targetPools)'
- 'Official Documentation: U(https://cloud.google.com/compute/docs/load-balancing/network/target-pools)'
'''

EXAMPLES = '''
- name: create a target pool
  gcp_compute_target_pool:
      name: "test_object"
      region: us-west1
      project: "test_project"
      auth_kind: "serviceaccount"
      service_account_file: "/tmp/auth.pem"
      state: present
'''

RETURN = '''
backupPool:
  description:
  - This field is applicable only when the containing target pool is serving a forwarding
    rule as the primary pool, and its failoverRatio field is properly set to a value
    between [0, 1].
  - 'backupPool and failoverRatio together define the fallback behavior of the primary
    target pool: if the ratio of the healthy instances in the primary pool is at or
    below failoverRatio, traffic arriving at the load-balanced IP will be directed
    to the backup pool.'
  - In case where failoverRatio and backupPool are not set, or all the instances in
    the backup pool are unhealthy, the traffic will be directed back to the primary
    pool in the "force" mode, where traffic will be spread to the healthy instances
    with the best effort, or to all instances when no instance is healthy.
  returned: success
  type: dict
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource.
  returned: success
  type: str
failoverRatio:
  description:
  - This field is applicable only when the containing target pool is serving a forwarding
    rule as the primary pool (i.e., not as a backup pool to some other target pool).
    The value of the field must be in [0, 1].
  - 'If set, backupPool must also be set. They together define the fallback behavior
    of the primary target pool: if the ratio of the healthy instances in the primary
    pool is at or below this number, traffic arriving at the load-balanced IP will
    be directed to the backup pool.'
  - In case where failoverRatio is not set or all the instances in the backup pool
    are unhealthy, the traffic will be directed back to the primary pool in the "force"
    mode, where traffic will be spread to the healthy instances with the best effort,
    or to all instances when no instance is healthy.
  returned: success
  type: str
healthCheck:
  description:
  - A reference to a HttpHealthCheck resource.
  - A member instance in this pool is considered healthy if and only if the health
    checks pass. If not specified it means all member instances will be considered
    healthy at all times.
  returned: success
  type: dict
id:
  description:
  - The unique identifier for the resource.
  returned: success
  type: int
instances:
  description:
  - A list of virtual machine instances serving this pool.
  - They must live in zones contained in the same region as this pool.
  returned: success
  type: list
name:
  description:
  - Name of the resource. Provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
sessionAffinity:
  description:
  - 'Session affinity option. Must be one of these values: - NONE: Connections from
    the same client IP may go to any instance in the pool.'
  - "- CLIENT_IP: Connections from the same client IP will go to the same instance
    in the pool while that instance remains healthy."
  - "- CLIENT_IP_PROTO: Connections from the same client IP with the same IP protocol
    will go to the same instance in the pool while that instance remains healthy."
  returned: success
  type: str
region:
  description:
  - The region where the target pool resides.
  returned: success
  type: str
'''
################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            backup_pool=dict(type='dict'),
            description=dict(type='str'),
            failover_ratio=dict(type='str'),
            health_check=dict(type='dict'),
            instances=dict(type='list', elements='dict'),
            name=dict(required=True, type='str'),
            session_affinity=dict(type='str', choices=['NONE', 'CLIENT_IP', 'CLIENT_IP_PROTO']),
            region=dict(required=True, type='str')
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#targetPool'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.put(link, resource_to_request(module)))


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#targetPool',
        u'backupPool': replace_resource_dict(module.params.get(u'backup_pool', {}), 'selfLink'),
        u'description': module.params.get('description'),
        u'failoverRatio': module.params.get('failover_ratio'),
        u'healthCheck': replace_resource_dict(module.params.get(u'health_check', {}), 'selfLink'),
        u'instances': replace_resource_dict(module.params.get('instances', []), 'selfLink'),
        u'name': module.params.get('name'),
        u'sessionAffinity': module.params.get('session_affinity')
    }
    request = encode_request(request, module)
    return_vals = {}
    for k, v in request.items():
        if v:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/targetPools/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/targetPools".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
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

    result = decode_request(result, module)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)
    request = decode_request(request, module)

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
    return {
        u'backupPool': replace_resource_dict(module.params.get(u'backup_pool', {}), 'selfLink'),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'failoverRatio': response.get(u'failoverRatio'),
        u'healthCheck': response.get(u'healthCheck'),
        u'id': response.get(u'id'),
        u'instances': response.get(u'instances'),
        u'name': module.params.get('name'),
        u'sessionAffinity': module.params.get('session_affinity')
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#targetPool')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], 'message')
        time.sleep(1.0)
        if status not in ['PENDING', 'RUNNING', 'DONE']:
            module.fail_json(msg="Invalid result %s" % status)
        op_result = fetch_resource(module, op_uri, 'compute#operation')
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


# Mask the fact healthChecks array is actually a single object of type
# HttpHealthCheck.
#
# Google Compute Engine API defines healthChecks as a list but it can only
# take [0, 1] elements. To make it simpler to declare we'll map that to a
# single object and encode/decode as appropriate.
def encode_request(request, module):
    if 'healthCheck' in request:
        request['healthChecks'] = [request['healthCheck']]
        del request['healthCheck']
    return request


# Mask healthChecks into a single element.
# @see encode_request for details
def decode_request(response, module):
    if response['kind'] != 'compute#targetPool':
        return response

    # Map healthChecks[0] => healthCheck
    if 'healthChecks' in response:
        if not response['healthChecks']:
            response['healthCheck'] = response['healthChecks'][0]
            del response['healthChecks']

    return response


if __name__ == '__main__':
    main()
