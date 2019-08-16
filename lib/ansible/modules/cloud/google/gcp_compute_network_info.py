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
module: gcp_compute_network_info
description:
- Gather info for GCP Network
- This module was called C(gcp_compute_network_facts) before Ansible 2.9. The usage
  has not changed.
short_description: Gather info for GCP Network
version_added: 2.7
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  filters:
    description:
    - A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/sdk/gcloud/reference/topic/filters).
    - Each additional filter in the list will act be added as an AND condition (filter1
      and filter2) .
    type: list
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: get info on a network
  gcp_compute_network_info:
    filters:
    - name = test_object
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
    description:
      description:
      - An optional description of this resource. The resource must be recreated to
        modify this field.
      returned: success
      type: str
    gateway_ipv4:
      description:
      - The gateway address for default routing out of the network. This value is
        selected by GCP.
      returned: success
      type: str
    id:
      description:
      - The unique identifier for the resource.
      returned: success
      type: int
    ipv4_range:
      description:
      - If this field is specified, a deprecated legacy network is created.
      - You will no longer be able to create a legacy network on Feb 1, 2020.
      - See the [legacy network docs](U(https://cloud.google.com/vpc/docs/legacy))
        for more details.
      - The range of internal addresses that are legal on this legacy network.
      - 'This range is a CIDR specification, for example: `192.168.0.0/16`.'
      - The resource must be recreated to modify this field.
      returned: success
      type: str
    name:
      description:
      - Name of the resource. Provided by the client when the resource is created.
        The name must be 1-63 characters long, and comply with RFC1035. Specifically,
        the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
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
      - When set to `true`, the network is created in "auto subnet mode" and it will
        create a subnet for each region automatically across the `10.128.0.0/9` address
        range.
      - When set to `false`, the network is created in "custom subnet mode" so the
        user can explicitly connect subnetwork resources.
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
          - The network-wide routing mode to use. If set to `REGIONAL`, this network's
            cloud routers will only advertise routes with subnetworks of this network
            in the same region as the router. If set to `GLOBAL`, this network's cloud
            routers will advertise routes with all subnetworks of this network, across
            regions.
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
    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str')))

    if module._name == 'gcp_compute_network_facts':
        module.deprecate("The 'gcp_compute_network_facts' module has been renamed to 'gcp_compute_network_info'", version='2.13')

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    return_value = {'resources': fetch_list(module, collection(module), query_options(module.params['filters']))}
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/networks".format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'compute')
    return auth.list(link, return_if_object, array_name='items', params={'filter': query})


def query_options(filters):
    if not filters:
        return ''

    if len(filters) == 1:
        return filters[0]
    else:
        queries = []
        for f in filters:
            # For multiple queries, all queries should have ()
            if f[0] != '(' and f[-1] != ')':
                queries.append("(%s)" % ''.join(f))
            else:
                queries.append(f)

        return ' '.join(queries)


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
