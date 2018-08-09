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
module: gcp_compute_instance_group_manager
description:
    - Creates a managed instance group using the information that you specify in the request.
      After the group is created, it schedules an action to create instances in the group
      using the specified instance template. This operation is marked as DONE when the
      group is created even if the instances in the group have not yet been created. You
      must separately verify the status of the individual instances.
    - A managed instance group can have up to 1000 VM instances per group.
short_description: Creates a GCP InstanceGroupManager
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
        choices: ['present', 'absent']
        default: 'present'
    base_instance_name:
        description:
            - The base instance name to use for instances in this group. The value must be 1-58
              characters long. Instances are named by appending a hyphen and a random four-character
              string to the base instance name.
            - The base instance name must comply with RFC1035.
        required: true
    description:
        description:
            - An optional description of this resource. Provide this property when you create
              the resource.
        required: false
    instance_template:
        description:
            - The instance template that is specified for this managed instance group. The group
              uses this template to create all new instances in the managed instance group.
        required: true
    name:
        description:
            - The name of the managed instance group. The name must be 1-63 characters long, and
              comply with RFC1035.
        required: true
    named_ports:
        description:
            - Named ports configured for the Instance Groups complementary to this Instance Group
              Manager.
        required: false
        suboptions:
            name:
                description:
                    - The name for this named port. The name must be 1-63 characters long, and comply
                      with RFC1035.
                required: false
            port:
                description:
                    - The port number, which can be a value between 1 and 65535.
                required: false
    target_pools:
        description:
            - TargetPool resources to which instances in the instanceGroup field are added. The
              target pools automatically apply to all of the instances in the managed instance
              group.
        required: false
    target_size:
        description:
            - The target number of running instances for this managed instance group. Deleting
              or abandoning instances reduces this number. Resizing the group changes this number.
        required: false
    zone:
        description:
            - The zone the managed instance group resides.
        required: true
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: create a network
  gcp_compute_network:
      name: "network-instancetemplate"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: network

- name: create a address
  gcp_compute_address:
      name: "address-instancetemplate"
      region: us-west1
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: address

- name: create a instance template
  gcp_compute_instance_template:
      name: "{{ resource_name }}"
      properties:
        disks:
        - auto_delete: true
          boot: true
          initialize_params:
            source_image: projects/ubuntu-os-cloud/global/images/family/ubuntu-1604-lts
        machine_type: n1-standard-1
        network_interfaces:
        - network: "{{ network }}"
          access_configs:
          - name: test-config
            type: ONE_TO_ONE_NAT
            nat_ip: "{{ address }}"
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: instancetemplate

- name: create a instance group manager
  gcp_compute_instance_group_manager:
      name: "test_object"
      base_instance_name: test1-child
      instance_template: "{{ instancetemplate }}"
      target_size: 3
      zone: us-west1-a
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present
'''

RETURN = '''
    base_instance_name:
        description:
            - The base instance name to use for instances in this group. The value must be 1-58
              characters long. Instances are named by appending a hyphen and a random four-character
              string to the base instance name.
            - The base instance name must comply with RFC1035.
        returned: success
        type: str
    creation_timestamp:
        description:
            - The creation timestamp for this managed instance group in RFC3339 text format.
        returned: success
        type: str
    current_actions:
        description:
            - The list of instance actions and the number of instances in this managed instance
              group that are scheduled for each of those actions.
        returned: success
        type: complex
        contains:
            abandoning:
                description:
                    - The total number of instances in the managed instance group that are scheduled to
                      be abandoned. Abandoning an instance removes it from the managed instance group
                      without deleting it.
                returned: success
                type: int
            creating:
                description:
                    - The number of instances in the managed instance group that are scheduled to be created
                      or are currently being created. If the group fails to create any of these instances,
                      it tries again until it creates the instance successfully.
                    - If you have disabled creation retries, this field will not be populated; instead,
                      the creatingWithoutRetries field will be populated.
                returned: success
                type: int
            creating_without_retries:
                description:
                    - The number of instances that the managed instance group will attempt to create.
                      The group attempts to create each instance only once. If the group fails to create
                      any of these instances, it decreases the group's targetSize value accordingly.
                returned: success
                type: int
            deleting:
                description:
                    - The number of instances in the managed instance group that are scheduled to be deleted
                      or are currently being deleted.
                returned: success
                type: int
            none:
                description:
                    - The number of instances in the managed instance group that are running and have
                      no scheduled actions.
                returned: success
                type: int
            recreating:
                description:
                    - The number of instances in the managed instance group that are scheduled to be recreated
                      or are currently being being recreated.
                    - Recreating an instance deletes the existing root persistent disk and creates a new
                      disk from the image that is defined in the instance template.
                returned: success
                type: int
            refreshing:
                description:
                    - The number of instances in the managed instance group that are being reconfigured
                      with properties that do not require a restart or a recreate action. For example,
                      setting or removing target pools for the instance.
                returned: success
                type: int
            restarting:
                description:
                    - The number of instances in the managed instance group that are scheduled to be restarted
                      or are currently being restarted.
                returned: success
                type: int
    description:
        description:
            - An optional description of this resource. Provide this property when you create
              the resource.
        returned: success
        type: str
    id:
        description:
            - A unique identifier for this resource.
        returned: success
        type: int
    instance_group:
        description:
            - The instance group being managed.
        returned: success
        type: dict
    instance_template:
        description:
            - The instance template that is specified for this managed instance group. The group
              uses this template to create all new instances in the managed instance group.
        returned: success
        type: dict
    name:
        description:
            - The name of the managed instance group. The name must be 1-63 characters long, and
              comply with RFC1035.
        returned: success
        type: str
    named_ports:
        description:
            - Named ports configured for the Instance Groups complementary to this Instance Group
              Manager.
        returned: success
        type: complex
        contains:
            name:
                description:
                    - The name for this named port. The name must be 1-63 characters long, and comply
                      with RFC1035.
                returned: success
                type: str
            port:
                description:
                    - The port number, which can be a value between 1 and 65535.
                returned: success
                type: int
    region:
        description:
            - The region this managed instance group resides (for regional resources).
        returned: success
        type: str
    target_pools:
        description:
            - TargetPool resources to which instances in the instanceGroup field are added. The
              target pools automatically apply to all of the instances in the managed instance
              group.
        returned: success
        type: list
    target_size:
        description:
            - The target number of running instances for this managed instance group. Deleting
              or abandoning instances reduces this number. Resizing the group changes this number.
        returned: success
        type: int
    zone:
        description:
            - The zone the managed instance group resides.
        returned: success
        type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import re
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            base_instance_name=dict(required=True, type='str'),
            description=dict(type='str'),
            instance_template=dict(required=True, type='dict'),
            name=dict(required=True, type='str'),
            named_ports=dict(type='list', elements='dict', options=dict(
                name=dict(type='str'),
                port=dict(type='int')
            )),
            target_pools=dict(type='list', elements='dict'),
            target_size=dict(type='int'),
            zone=dict(required=True, type='str')
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#instanceGroupManager'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                fetch = update(module, self_link(module), kind)
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
        u'kind': 'compute#instanceGroupManager',
        u'baseInstanceName': module.params.get('base_instance_name'),
        u'description': module.params.get('description'),
        u'instanceTemplate': replace_resource_dict(module.params.get(u'instance_template', {}), 'selfLink'),
        u'name': module.params.get('name'),
        u'namedPorts': InstGrouManaNamePortArray(module.params.get('named_ports', []), module).to_request(),
        u'targetPools': replace_resource_dict(module.params.get('target_pools', []), 'selfLink'),
        u'targetSize': module.params.get('target_size')
    }
    return_vals = {}
    for k, v in request.items():
        if v:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers".format(**module.params)


def return_if_object(module, response, kind):
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
    if result['kind'] != kind:
        module.fail_json(msg="Incorrect result: {kind}".format(**result))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

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
        u'baseInstanceName': response.get(u'baseInstanceName'),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'currentActions': InstGrouManaCurrActi(response.get(u'currentActions', {}), module).from_response(),
        u'description': module.params.get('description'),
        u'id': response.get(u'id'),
        u'instanceGroup': response.get(u'instanceGroup'),
        u'instanceTemplate': response.get(u'instanceTemplate'),
        u'name': response.get(u'name'),
        u'namedPorts': InstGrouManaNamePortArray(response.get(u'namedPorts', []), module).from_response(),
        u'region': response.get(u'region'),
        u'targetPools': response.get(u'targetPools'),
        u'targetSize': response.get(u'targetSize')
    }


def region_selflink(name, params):
    if name is None:
        return
    url = r"https://www.googleapis.com/compute/v1/projects/.*/regions/[a-z1-9\-]*"
    if not re.match(url, name):
        name = "https://www.googleapis.com/compute/v1/projects/{project}/regions/%s".format(**params) % name
    return name


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#instanceGroupManager')


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


class InstGrouManaCurrActi(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({
            u'abandoning': self.request.get('abandoning'),
            u'creating': self.request.get('creating'),
            u'creatingWithoutRetries': self.request.get('creating_without_retries'),
            u'deleting': self.request.get('deleting'),
            u'none': self.request.get('none'),
            u'recreating': self.request.get('recreating'),
            u'refreshing': self.request.get('refreshing'),
            u'restarting': self.request.get('restarting')
        })

    def from_response(self):
        return remove_nones_from_dict({
            u'abandoning': self.request.get(u'abandoning'),
            u'creating': self.request.get(u'creating'),
            u'creatingWithoutRetries': self.request.get(u'creatingWithoutRetries'),
            u'deleting': self.request.get(u'deleting'),
            u'none': self.request.get(u'none'),
            u'recreating': self.request.get(u'recreating'),
            u'refreshing': self.request.get(u'refreshing'),
            u'restarting': self.request.get(u'restarting')
        })


class InstGrouManaNamePortArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({
            u'name': item.get('name'),
            u'port': item.get('port')
        })

    def _response_from_item(self, item):
        return remove_nones_from_dict({
            u'name': item.get(u'name'),
            u'port': item.get(u'port')
        })


if __name__ == '__main__':
    main()
