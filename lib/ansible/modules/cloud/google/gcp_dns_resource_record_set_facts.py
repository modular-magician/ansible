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
module: gcp_dns_resource_record_set_facts
description:
  - Gather facts for GCP ResourceRecordSet
short_description: Gather facts for GCP ResourceRecordSet
version_added: 2.7
author: Google Inc. (@googlecloudplatform)
requirements:
    - python >= 2.6
    - requests >= 2.18.4
    - google-auth >= 1.3.0
options:
    managed_zone:
        description:
            - Identifies the managed zone addressed by this request.
            - Can be the managed zone name or id.
        required: true
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name:  a resource record set facts
  gcp_dns_resource_record_set_facts:
      managed_zone: "{{ managed_zone }}"
      project: test_project
      auth_kind: service_account
      service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
items:
    description: List of items
    returned: always
    type: complex
    contains:
        name:
            description:
                - For example, U(www.example.com.)
            returned: success
            type: str
        type:
            description:
                - One of valid DNS resource types.
            returned: success
            type: str
        ttl:
            description:
                - Number of seconds that this ResourceRecordSet can be cached by resolvers.
            returned: success
            type: int
        target:
            description:
                - As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) .
            returned: success
            type: list
        managed_zone:
            description:
                - Identifies the managed zone addressed by this request.
                - Can be the managed zone name or id.
            returned: success
            type: dict
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
    module = GcpModule(
        argument_spec=dict(
            managed_zone=dict(required=True, type='dict')
        )
    )

    if 'scopes' not in module.params:
        module.params['scopes'] = ['https://www.googleapis.com/auth/ndev.clouddns.readwrite']

    items = fetch_list(module, collection(module))
    if items.get('rrsets'):
        items = items.get('rrsets')
    else:
        items = []
    return_value = {
        'items': items
    }
    module.exit_json(**return_value)


def collection(module):
    res = {
        'project': module.params['project'],
        'managed_zone': replace_resource_dict(module.params['managed_zone'], 'name')
    }
    return "https://www.googleapis.com/dns/v1/projects/{project}/managedZones/{managed_zone}/rrsets".format(**res)


def fetch_list(module, link):
    auth = GcpSession(module, 'dns')
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
