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

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
lookup: gcp_lookup
author:
  - Google (@googlecloudplatform)
version_added: "2.6"
requirements:
  - python >= 2.6
  - requests >= 2.18.4
  - google-auth >= 1.3.0
extends_documentation_fragment:
  - gcp
short_description: Look up and verify GCP Attributes
description:
  - Describes attributes on GCP. You can specify one of the listed
    attribute choices or omit it to see all attributes.
options:
  attribute:
    description: The attribute for which to get the value(s).
    default: null
    choices:
      - disk_type
      - license
      - machine_type
      - region
      - zone
      - instance_config
  return:
    description: An optional value to describe what part of the attribute should
                 be returned
    default: null
"""

EXAMPLES = """
vars:
  account_details: "{{ lookup('gcp_lookup',
                              attribute='region',
                              label='us-west1',
                              auth_kind='serviceaccount',
                              service_account_file='/tmp/my_account.json',
                              project='test-project',
                              scopes=['https://www.googleapis.com/auth/compute']) }}"
  # us-west1
  account_details: "{{ lookup('gcp_lookup',
                              attribute='region',
                              return='self_link',
                              label='us-west1',
                              auth_kind='serviceaccount',
                              service_account_file='/tmp/my_account.json',
                              project='test-project',
                              scopes=['https://www.googleapis.com/auth/compute']) }}"
  # us-west1

"""

RETURN = """
"""


################################################################################
# Imports
################################################################################

from ansible.errors import AnsibleError
from ansible.plugins import AnsiblePlugin
from ansible.plugins.lookup import LookupBase
from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpRequestException
import json

################################################################################
# Main
################################################################################


class GcpModule(object):
    def __init__(self, options):
        self.params = options
        if 'label' in self.params:
            self.params['name'] = self.params['label']
            del self.params['label']

    def fail_json(self, **kwargs):
        raise AnsibleError(kwargs['msg'])


class GcpDiskType(object):
    def __init__(self, options):
        self.module = GcpModule(options)

        self.kind = 'compute#diskType'
        self.link = "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/diskTypes/{name}".format(**self.module.params)

    def _fetch_resource(self):
        auth = GcpSession(self.module, 'compute')
        return self._return_if_object(auth.get(self.link))

    def _return_if_object(self, response):
        # If not found, return nothing.
        if response.status_code == 404:
            return None

        # If no content, return nothing.
        if response.status_code == 204:
            return None

        try:
            response.raise_for_status
            result = response.json()
        except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
            self.module.fail_json(msg="Invalid JSON response with error: %s" % inst)
        except GcpRequestException as inst:
            self.module.fail_json(msg="Network error: %s" % inst)

        if navigate_hash(result, ['error', 'errors']):
            self.module.fail_json(msg=navigate_hash(result, ['error', 'errors']))
        if result['kind'] != self.kind:
            self.module.fail_json(msg="Incorrect result: {kind}".format(**result))

        return result

    def run(self):
        response = self._fetch_resource()
        if 'return' in self.module.params:
            return response[self.module.params['return']]
        return response['self_link']


class GcpLicense(object):
    def __init__(self, options):
        self.module = GcpModule(options)

        self.kind = 'compute#license'
        self.link = "https://www.googleapis.com/compute/v1//projects/{project}/global/licenses/{name}".format(**self.module.params)

    def _fetch_resource(self):
        auth = GcpSession(self.module, 'compute')
        return self._return_if_object(auth.get(self.link))

    def _return_if_object(self, response):
        # If not found, return nothing.
        if response.status_code == 404:
            return None

        # If no content, return nothing.
        if response.status_code == 204:
            return None

        try:
            response.raise_for_status
            result = response.json()
        except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
            self.module.fail_json(msg="Invalid JSON response with error: %s" % inst)
        except GcpRequestException as inst:
            self.module.fail_json(msg="Network error: %s" % inst)

        if navigate_hash(result, ['error', 'errors']):
            self.module.fail_json(msg=navigate_hash(result, ['error', 'errors']))
        if result['kind'] != self.kind:
            self.module.fail_json(msg="Incorrect result: {kind}".format(**result))

        return result

    def run(self):
        response = self._fetch_resource()
        if 'return' in self.module.params:
            return response[self.module.params['return']]
        return response['self_link']


class GcpMachineType(object):
    def __init__(self, options):
        self.module = GcpModule(options)

        self.kind = 'compute#machineType'
        self.link = "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/machineTypes/{name}".format(**self.module.params)

    def _fetch_resource(self):
        auth = GcpSession(self.module, 'compute')
        return self._return_if_object(auth.get(self.link))

    def _return_if_object(self, response):
        # If not found, return nothing.
        if response.status_code == 404:
            return None

        # If no content, return nothing.
        if response.status_code == 204:
            return None

        try:
            response.raise_for_status
            result = response.json()
        except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
            self.module.fail_json(msg="Invalid JSON response with error: %s" % inst)
        except GcpRequestException as inst:
            self.module.fail_json(msg="Network error: %s" % inst)

        if navigate_hash(result, ['error', 'errors']):
            self.module.fail_json(msg=navigate_hash(result, ['error', 'errors']))
        if result['kind'] != self.kind:
            self.module.fail_json(msg="Incorrect result: {kind}".format(**result))

        return result

    def run(self):
        response = self._fetch_resource()
        if 'return' in self.module.params:
            return response[self.module.params['return']]
        return response['name']


class GcpRegion(object):
    def __init__(self, options):
        self.module = GcpModule(options)

        self.kind = 'compute#region'
        self.link = "https://www.googleapis.com/compute/v1/projects/{project}/regions/{name}".format(**self.module.params)

    def _fetch_resource(self):
        auth = GcpSession(self.module, 'compute')
        return self._return_if_object(auth.get(self.link))

    def _return_if_object(self, response):
        # If not found, return nothing.
        if response.status_code == 404:
            return None

        # If no content, return nothing.
        if response.status_code == 204:
            return None

        try:
            response.raise_for_status
            result = response.json()
        except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
            self.module.fail_json(msg="Invalid JSON response with error: %s" % inst)
        except GcpRequestException as inst:
            self.module.fail_json(msg="Network error: %s" % inst)

        if navigate_hash(result, ['error', 'errors']):
            self.module.fail_json(msg=navigate_hash(result, ['error', 'errors']))
        if result['kind'] != self.kind:
            self.module.fail_json(msg="Incorrect result: {kind}".format(**result))

        return result

    def run(self):
        response = self._fetch_resource()
        if 'return' in self.module.params:
            return response[self.module.params['return']]
        return response['name']


class GcpZone(object):
    def __init__(self, options):
        self.module = GcpModule(options)

        self.kind = 'compute#zone'
        self.link = "https://www.googleapis.com/compute/v1/projects/{project}/zones/{name}".format(**self.module.params)

    def _fetch_resource(self):
        auth = GcpSession(self.module, 'compute')
        return self._return_if_object(auth.get(self.link))

    def _return_if_object(self, response):
        # If not found, return nothing.
        if response.status_code == 404:
            return None

        # If no content, return nothing.
        if response.status_code == 204:
            return None

        try:
            response.raise_for_status
            result = response.json()
        except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
            self.module.fail_json(msg="Invalid JSON response with error: %s" % inst)
        except GcpRequestException as inst:
            self.module.fail_json(msg="Network error: %s" % inst)

        if navigate_hash(result, ['error', 'errors']):
            self.module.fail_json(msg=navigate_hash(result, ['error', 'errors']))
        if result['kind'] != self.kind:
            self.module.fail_json(msg="Incorrect result: {kind}".format(**result))

        return result

    def run(self):
        response = self._fetch_resource()
        if 'return' in self.module.params:
            return response[self.module.params['return']]
        return response['name']


class GcpInstanceConfig(object):
    def __init__(self, options):
        self.module = GcpModule(options)

        self.link = "https://spanner.googleapis.com/v1/projects/{project}/instanceConfigs/{name}".format(**self.module.params)

    def _fetch_resource(self):
        auth = GcpSession(self.module, 'spanner')
        return self._return_if_object(auth.get(self.link))

    def _return_if_object(self, response):
        # If not found, return nothing.
        if response.status_code == 404:
            return None

        # If no content, return nothing.
        if response.status_code == 204:
            return None

        try:
            response.raise_for_status
            result = response.json()
        except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
            self.module.fail_json(msg="Invalid JSON response with error: %s" % inst)
        except GcpRequestException as inst:
            self.module.fail_json(msg="Network error: %s" % inst)

        if navigate_hash(result, ['error', 'errors']):
            self.module.fail_json(msg=navigate_hash(result, ['error', 'errors']))
        if result['kind'] != self.kind:
            self.module.fail_json(msg="Incorrect result: {kind}".format(**result))

        return result

    def run(self):
        response = self._fetch_resource()
        if 'return' in self.module.params:
            return response[self.module.params['return']]
        return response['name']


class LookupModule(LookupBase):
    def run(self, terms, variables, **kwargs):

        self.set_options(var_options=variables, direct=kwargs)
        options = {
            'disk_type': GcpDiskType,
            'license': GcpLicense,
            'machine_type': GcpMachineType,
            'region': GcpRegion,
            'zone': GcpZone,
            'instance_config': GcpInstanceConfig
        }

        return str(options[kwargs['attribute']](kwargs).run())
