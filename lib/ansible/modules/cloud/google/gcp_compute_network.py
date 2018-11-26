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
module: gcp_compute_network
description:
- Represents a Network resource.
- Your Cloud Platform Console project can contain multiple networks, and each network
  can have multiple instances attached to it. A network allows you to define a gateway
  IP and the network range for the instances attached to that network. Every project
  is provided with a default network with preset configurations and firewall rules.
  You can choose to customize the default network by adding or removing rules, or
  you can create new networks in that project. Generally, most users only need one
  network, although you can have up to five networks per project by default.
- A network belongs to only one project, and each instance can only belong to one
  network. All Compute Engine networks use the IPv4 protocol. Compute Engine currently
  does not support IPv6. However, Google is a major advocate of IPv6 and it is an
  important future direction.
short_description: Creates a GCP Network
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
  description:
    description:
    - An optional description of this resource. Provide this property when you create
      the resource.
    required: false
  ipv4_range:
    description:
    - 'The range of internal addresses that are legal on this network. This range
      is a CIDR specification, for example: 192.168.0.0/16. Provided by the client
      when the network is created.'
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
  auto_create_subnetworks:
    description:
    - When set to true, the network is created in "auto subnet mode". When set to
      false, the network is in "custom subnet mode".
    - In "auto subnet mode", a newly created network is assigned the default CIDR
      of 10.128.0.0/9 and it automatically creates one subnetwork per region.
    required: false
    type: bool
  routing_config:
    description:
    - The network-level routing configuration for this network. Used by Cloud Router
      to determine what type of network-wide routing behavior to enforce.
    required: false
    version_added: 2.8
    suboptions:
      routing_mode:
        description:
        - The network-wide routing mode to use. If set to REGIONAL, this network's
          cloud routers will only advertise routes with subnetworks of this network
          in the same region as the router. If set to GLOBAL, this network's cloud
          routers will advertise routes with all subnetworks of this network, across
          regions.
        required: true
        choices:
        - REGIONAL
        - GLOBAL
extends_documentation_fragment: gcp
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/rest/v1/networks)'
- 'Official Documentation: U(https://cloud.google.com/vpc/docs/vpc)'
'''

EXAMPLES = '''
- name: create a network
  gcp_compute_network:
      name: "test_object"
      auto_create_subnetworks: true
      project: "test_project"
      auth_kind: "serviceaccount"
      service_account_file: "/tmp/auth.pem"
      state: present
'''

RETURN = '''
description:
  description:
  - An optional description of this resource. Provide this property when you create
    the resource.
  returned: success
  type: str
gateway_ipv4:
  description:
  - A gateway address for default routing to other networks. This value is read only
    and is selected by the Google Compute Engine, typically as the first usable address
    in the IPv4Range.
  returned: success
  type: str
id:
  description:
  - The unique identifier for the resource.
  returned: success
  type: int
ipv4_range:
  description:
  - 'The range of internal addresses that are legal on this network. This range is
    a CIDR specification, for example: 192.168.0.0/16. Provided by the client when
    the network is created.'
  returned: success
  type: str
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
subnetworks:
  description:
  - Server-defined fully-qualified URLs for all subnetworks in this network.
  returned: success
  type: list
autoCreateSubnetworks:
  description:
  - When set to true, the network is created in "auto subnet mode". When set to false,
    the network is in "custom subnet mode".
  - In "auto subnet mode", a newly created network is assigned the default CIDR of
    10.128.0.0/9 and it automatically creates one subnetwork per region.
  returned: success
  type: bool
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
routingConfig:
  description:
  - The network-level routing configuration for this network. Used by Cloud Router
    to determine what type of network-wide routing behavior to enforce.
  returned: success
  type: complex
  contains:
    routingMode:
      description:
      - The network-wide routing mode to use. If set to REGIONAL, this network's cloud
        routers will only advertise routes with subnetworks of this network in the
        same region as the router. If set to GLOBAL, this network's cloud routers
        will advertise routes with all subnetworks of this network, across regions.
      returned: success
      type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
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
            description=dict(type='str'),
            ipv4_range=dict(type='str'),
            name=dict(required=True, type='str'),
            auto_create_subnetworks=dict(type='bool'),
            routing_config=dict(type='list', elements='dict', options=dict(
                routing_mode=dict(required=True, type='str', choices=['REGIONAL', 'GLOBAL'])
            ))
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#network'

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
    return wait_for_operation(module, auth.patch(link, resource_to_request(module)))


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#network',
        u'description': module.params.get('description'),
        u'IPv4Range': module.params.get('ipv4_range'),
        u'name': module.params.get('name'),
        u'autoCreateSubnetworks': module.params.get('auto_create_subnetworks'),
        u'routingConfig': NetworkRoutingconfigArray(module.params.get('routing_config', []), module).to_request()
    }
    return_vals = {}
    for k, v in request.items():
        if v:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/networks".format(**module.params)


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

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

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
        u'description': module.params.get('description'),
        u'gatewayIPv4': response.get(u'gateway_ipv4'),
        u'id': response.get(u'id'),
        u'IPv4Range': module.params.get('ipv4_range'),
        u'name': module.params.get('name'),
        u'subnetworks': response.get(u'subnetworks'),
        u'autoCreateSubnetworks': module.params.get('auto_create_subnetworks'),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'routingConfig': NetworkRoutingconfigArray(response.get(u'routingConfig', []), module).from_response()
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/global/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#network')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], 'message')
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation')
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class NetworkRoutingconfigArray(object):
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
            u'routingMode': item.get('routing_mode')
        })

    def _response_from_item(self, item):
        return remove_nones_from_dict({
            u'routingMode': item.get(u'routingMode')
        })


if __name__ == '__main__':
    main()
