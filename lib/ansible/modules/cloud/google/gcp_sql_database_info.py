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
module: gcp_sql_database_info
description:
- Gather info for GCP Database
- This module was called C(gcp_sql_database_facts) before Ansible 2.9. The usage has
  not changed.
short_description: Gather info for GCP Database
version_added: 2.8
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  instance:
    description:
    - The name of the Cloud SQL instance. This does not include the project ID.
    required: true
    type: str
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: get info on a database
  gcp_sql_database_info:
    instance: "{{ instance }}"
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
    charset:
      description:
      - The charset value. See MySQL's [Supported Character Sets and Collations](U(https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html))
        and Postgres' [Character Set Support](U(https://www.postgresql.org/docs/9.6/static/multibyte.html))
        for more details and supported values. Postgres databases only support a value
        of `UTF8` at creation time.
      returned: success
      type: str
    collation:
      description:
      - The collation value. See MySQL's [Supported Character Sets and Collations](U(https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html))
        and Postgres' [Collation Support](U(https://www.postgresql.org/docs/9.6/static/collation.html))
        for more details and supported values. Postgres databases only support a value
        of `en_US.UTF8` at creation time.
      returned: success
      type: str
    name:
      description:
      - The name of the database in the Cloud SQL instance.
      - This does not include the project ID or instance name.
      returned: success
      type: str
    instance:
      description:
      - The name of the Cloud SQL instance. This does not include the project ID.
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
    module = GcpModule(argument_spec=dict(instance=dict(required=True, type='str')))

    if module._name == 'gcp_sql_database_facts':
        module.deprecate("The 'gcp_sql_database_facts' module has been renamed to 'gcp_sql_database_info'", version='2.13')

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/sqlservice.admin']

    items = fetch_list(module, collection(module))
    if items.get('items'):
        items = items.get('items')
    else:
        items = []
    return_value = {'resources': items}
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}/databases".format(**module.params)


def fetch_list(module, link):
    auth = GcpSession(module, 'sql')
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
