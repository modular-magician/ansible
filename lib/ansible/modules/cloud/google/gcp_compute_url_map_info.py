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
module: gcp_compute_url_map_info
description:
- Gather info for GCP UrlMap
- This module was called C(gcp_compute_url_map_facts) before Ansible 2.9. The usage
  has not changed.
short_description: Gather info for GCP UrlMap
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
- name: get info on an URL map
  gcp_compute_url_map_info:
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
    creationTimestamp:
      description:
      - Creation timestamp in RFC3339 text format.
      returned: success
      type: str
    defaultService:
      description:
      - A reference to BackendService resource if none of the hostRules match.
      returned: success
      type: dict
    description:
      description:
      - An optional description of this resource. Provide this property when you create
        the resource.
      returned: success
      type: str
    hostRules:
      description:
      - The list of HostRules to use against the URL.
      returned: success
      type: complex
      contains:
        description:
          description:
          - An optional description of this HostRule. Provide this property when you
            create the resource.
          returned: success
          type: str
        hosts:
          description:
          - The list of host patterns to match. They must be valid hostnames, except
            * will match any string of ([a-z0-9-.]*). In that case, * must be the
            first character and must be followed in the pattern by either - or .
          returned: success
          type: list
        pathMatcher:
          description:
          - The name of the PathMatcher to use to match the path portion of the URL
            if the hostRule matches the URL's host portion.
          returned: success
          type: str
    id:
      description:
      - The unique identifier for the resource.
      returned: success
      type: int
    fingerprint:
      description:
      - Fingerprint of this resource. This field is used internally during updates
        of this resource.
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
    pathMatchers:
      description:
      - The list of named PathMatchers to use against the URL.
      returned: success
      type: complex
      contains:
        defaultService:
          description:
          - A reference to a BackendService resource. This will be used if none of
            the pathRules defined by this PathMatcher is matched by the URL's path
            portion.
          returned: success
          type: dict
        description:
          description:
          - An optional description of this resource.
          returned: success
          type: str
        name:
          description:
          - The name to which this PathMatcher is referred by the HostRule.
          returned: success
          type: str
        pathRules:
          description:
          - The list of path rules.
          returned: success
          type: complex
          contains:
            paths:
              description:
              - 'The list of path patterns to match. Each must start with / and the
                only place a * is allowed is at the end following a /. The string
                fed to the path matcher does not include any text after the first
                ? or #, and those chars are not allowed here.'
              returned: success
              type: list
            service:
              description:
              - A reference to the BackendService resource if this rule is matched.
              returned: success
              type: dict
    tests:
      description:
      - The list of expected URL mappings. Requests to update this UrlMap will succeed
        only if all of the test cases pass.
      returned: success
      type: complex
      contains:
        description:
          description:
          - Description of this test case.
          returned: success
          type: str
        host:
          description:
          - Host portion of the URL.
          returned: success
          type: str
        path:
          description:
          - Path portion of the URL.
          returned: success
          type: str
        service:
          description:
          - A reference to expected BackendService resource the given URL should be
            mapped to.
          returned: success
          type: dict
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

    if module._name == 'gcp_compute_url_map_facts':
        module.deprecate("The 'gcp_compute_url_map_facts' module has been renamed to 'gcp_compute_url_map_info'", version='2.13')

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    items = fetch_list(module, collection(module), query_options(module.params['filters']))
    if items.get('items'):
        items = items.get('items')
    else:
        items = []
    return_value = {'resources': items}
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/urlMaps".format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'compute')
    response = auth.get(link, params={'filter': query})
    return return_if_object(module, response)


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
