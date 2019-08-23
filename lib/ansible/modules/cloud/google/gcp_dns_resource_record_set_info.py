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
module: gcp_dns_resource_record_set_info
description:
- Gather info for GCP ResourceRecordSet
- This module was called C(gcp_dns_resource_record_set_facts) before Ansible 2.9.
  The usage has not changed.
short_description: Gather info for GCP ResourceRecordSet
version_added: 2.8
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  managed_zone:
    description:
    - Identifies the managed zone addressed by this request.
    - 'This field represents a link to a ManagedZone resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''name'' and value of
      your resource''s name Alternatively, you can add `register: name-of-resource`
      to a gcp_dns_managed_zone task and then set this managed_zone field to "{{ name-of-resource
      }}"'
    required: true
    type: dict
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: get info on a resource record set
  gcp_dns_resource_record_set_info:
    managed_zone: "{{ managed_zone }}"
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
      - For example, U(www.example.com).
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
    module = GcpModule(argument_spec=dict(managed_zone=dict(required=True, type='dict')))

    if module._name == 'gcp_dns_resource_record_set_facts':
        module.deprecate("The 'gcp_dns_resource_record_set_facts' module has been renamed to 'gcp_dns_resource_record_set_info'", version='2.13')

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/ndev.clouddns.readwrite']

    return_value = {'resources': fetch_list(module, collection(module))}
    module.exit_json(**return_value)


def collection(module):
    res = {'project': module.params['project'], 'managed_zone': replace_resource_dict(module.params['managed_zone'], 'name')}
    return "https://www.googleapis.com/dns/v1/projects/{project}/managedZones/{managed_zone}/rrsets".format(**res)


def fetch_list(module, link):
    auth = GcpSession(module, 'dns')
    return auth.list(link, return_if_object, array_name='rrsets')


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
