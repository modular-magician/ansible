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
module: gcp_compute_instance_group_facts
description:
  - Gather facts for GCP InstanceGroup
short_description: Gather facts for GCP InstanceGroup
version_added: 2.7
author: Google Inc. (@googlecloudplatform)
requirements:
    - python >= 2.6
    - requests >= 2.18.4
    - google-auth >= 1.3.0
options:
    zone:
        description:
            - A reference to the zone where the instance group resides.
        required: true
extends_documentation_fragment: gcp
'''

################################################################################
# Imports
################################################################################
from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest

################################################################################
# Main
################################################################################
def main():
    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            filters=dict(type='list', elements='str'),
            zone=dict(required=True, type='str')
        )
    )

    items = fetch_list(module, collection(module), query_options(module.params['filters']))
    if items.get('items'):
        items = items.get('items')  
    else:
        items = []
    return_value = {
      'items': items
    }
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instanceGroups".format(**module.params)

def fetch_list(module, link, query):
    auth = GcpSession(module, 'compute')
    response = auth.get(link, params={'filter': query})
    return return_if_object(module, response)


def query_options(filters):
    '''
        :param config_data: contents of the inventory config file
        :return A fully built query string
    '''
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
    if result['kind'] != 'compute#instanceGroupList':
        module.fail_json(msg="Incorrect result: {kind}".format(**result))

    return result
if __name__ == "__main__":
    main()
