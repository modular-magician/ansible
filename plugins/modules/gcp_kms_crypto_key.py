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
module: gcp_kms_crypto_key
description:
- A `CryptoKey` represents a logical key that can be used for cryptographic operations.
short_description: Creates a GCP CryptoKey
version_added: '2.9'
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
    type: str
  name:
    description:
    - The resource name for the CryptoKey.
    required: true
    type: str
  labels:
    description:
    - Labels with user-defined metadata to apply to this resource.
    required: false
    type: dict
  purpose:
    description:
    - Immutable purpose of CryptoKey. See U(https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose)
      for inputs.
    - 'Some valid choices include: "ENCRYPT_DECRYPT", "ASYMMETRIC_SIGN", "ASYMMETRIC_DECRYPT"'
    required: false
    default: ENCRYPT_DECRYPT
    type: str
  rotation_period:
    description:
    - Every time this period passes, generate a new CryptoKeyVersion and set it as
      the primary.
    - The first rotation will take place after the specified period. The rotation
      period has the format of a decimal number with up to 9 fractional digits, followed
      by the letter `s` (seconds). It must be greater than a day (ie, 86400).
    required: false
    type: str
  version_template:
    description:
    - A template describing settings for new crypto key versions.
    required: false
    type: dict
    suboptions:
      algorithm:
        description:
        - The algorithm to use when creating a version based on this template.
        - See the [algorithm reference](U(https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm))
          for possible inputs.
        required: true
        type: str
      protection_level:
        description:
        - The protection level to use when creating a version based on this template.
        - 'Some valid choices include: "SOFTWARE", "HSM"'
        required: false
        type: str
  key_ring:
    description:
    - The KeyRing that this key belongs to.
    - 'Format: `''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}''`.'
    required: true
    type: str
extends_documentation_fragment: gcp
notes:
- 'API Reference: U(https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys)'
- 'Creating a key: U(https://cloud.google.com/kms/docs/creating-keys#create_a_key)'
'''

EXAMPLES = '''
- name: create a key ring
  gcp_kms_key_ring:
    name: key-key-ring
    location: us-central1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: keyring

- name: create a crypto key
  gcp_kms_crypto_key:
    name: test_object
    key_ring: projects/{{ gcp_project }}/locations/us-central1/keyRings/key-key-ring
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - The resource name for the CryptoKey.
  returned: success
  type: str
creationTime:
  description:
  - The time that this resource was created on the server.
  - This is in RFC3339 text format.
  returned: success
  type: str
labels:
  description:
  - Labels with user-defined metadata to apply to this resource.
  returned: success
  type: dict
purpose:
  description:
  - Immutable purpose of CryptoKey. See U(https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose)
    for inputs.
  returned: success
  type: str
rotationPeriod:
  description:
  - Every time this period passes, generate a new CryptoKeyVersion and set it as the
    primary.
  - The first rotation will take place after the specified period. The rotation period
    has the format of a decimal number with up to 9 fractional digits, followed by
    the letter `s` (seconds). It must be greater than a day (ie, 86400).
  returned: success
  type: str
versionTemplate:
  description:
  - A template describing settings for new crypto key versions.
  returned: success
  type: complex
  contains:
    algorithm:
      description:
      - The algorithm to use when creating a version based on this template.
      - See the [algorithm reference](U(https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm))
        for possible inputs.
      returned: success
      type: str
    protectionLevel:
      description:
      - The protection level to use when creating a version based on this template.
      returned: success
      type: str
keyRing:
  description:
  - The KeyRing that this key belongs to.
  - 'Format: `''projects/{{project}}/locations/{{location}}/keyRings/{{keyRing}}''`.'
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            labels=dict(type='dict'),
            purpose=dict(default='ENCRYPT_DECRYPT', type='str'),
            rotation_period=dict(type='str'),
            version_template=dict(type='dict', options=dict(algorithm=dict(required=True, type='str'), protection_level=dict(type='str'))),
            key_ring=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloudkms']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), fetch)
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, create_link(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'kms')
    return return_if_object(module, auth.post(link, resource_to_request(module)))


def update(module, link, fetch):
    auth = GcpSession(module, 'kms')
    params = {'updateMask': updateMask(resource_to_request(module), response_to_hash(module, fetch))}
    request = resource_to_request(module)
    return return_if_object(module, auth.patch(link, request, params=params))


def updateMask(request, response):
    update_mask = []
    if request.get('labels') != response.get('labels'):
        update_mask.append('labels')
    if request.get('rotationPeriod') != response.get('rotationPeriod'):
        update_mask.append('rotationPeriod')
    if request.get('versionTemplate') != response.get('versionTemplate'):
        update_mask.append('versionTemplate')
    return ','.join(update_mask)


def delete(module, link):
    module.fail_json(msg="KeyRings cannot be deleted")


def resource_to_request(module):
    request = {
        u'labels': module.params.get('labels'),
        u'purpose': module.params.get('purpose'),
        u'rotationPeriod': module.params.get('rotation_period'),
        u'versionTemplate': CryptoKeyVersiontemplate(module.params.get('version_template', {}), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'kms')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://cloudkms.googleapis.com/v1/{key_ring}/cryptoKeys/{name}".format(**module.params)


def collection(module):
    return "https://cloudkms.googleapis.com/v1/{key_ring}/cryptoKeys".format(**module.params)


def create_link(module):
    return "https://cloudkms.googleapis.com/v1/{key_ring}/cryptoKeys?cryptoKeyId={name}".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    result = decode_response(result, module)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)
    request = decode_response(request, module)

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
        u'name': module.params.get('name'),
        u'creationTime': response.get(u'creationTime'),
        u'labels': response.get(u'labels'),
        u'purpose': module.params.get('purpose'),
        u'rotationPeriod': response.get(u'rotationPeriod'),
        u'versionTemplate': CryptoKeyVersiontemplate(response.get(u'versionTemplate', {}), module).from_response(),
    }


def decode_response(response, module):
    if 'name' in response:
        response['name'] = response['name'].split('/')[-1]
    return response


class CryptoKeyVersiontemplate(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'algorithm': self.request.get('algorithm'), u'protectionLevel': self.request.get('protection_level')})

    def from_response(self):
        return remove_nones_from_dict({u'algorithm': self.request.get(u'algorithm'), u'protectionLevel': self.module.params.get('protection_level')})


if __name__ == '__main__':
    main()
