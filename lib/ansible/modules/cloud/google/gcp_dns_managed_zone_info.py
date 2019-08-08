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
module: gcp_dns_managed_zone_info
description:
- Gather info for GCP ManagedZone
- This module was called C({{ old_name }}) before Ansible 2.9. The usage has not changed.
short_description: Gather info for GCP ManagedZone
version_added: 2.8
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  dns_name:
    description:
    - Restricts the list to return only zones with this domain name.
    type: list
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: get info on a managed zone
  gcp_dns_managed_zone_info:
    dns_name: test.somewild2.example.com.
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
      - A mutable string of at most 1024 characters associated with this resource
        for the user's convenience. Has no effect on the managed zone's function.
      returned: success
      type: str
    dnsName:
      description:
      - The DNS name of this managed zone, for instance "example.com.".
      returned: success
      type: str
    dnssecConfig:
      description:
      - DNSSEC configuration.
      returned: success
      type: complex
      contains:
        kind:
          description:
          - Identifies what kind of resource this is.
          returned: success
          type: str
        nonExistence:
          description:
          - Specifies the mechanism used to provide authenticated denial-of-existence
            responses.
          returned: success
          type: str
        state:
          description:
          - Specifies whether DNSSEC is enabled, and what mode it is in.
          returned: success
          type: str
        defaultKeySpecs:
          description:
          - Specifies parameters that will be used for generating initial DnsKeys
            for this ManagedZone. If you provide a spec for keySigning or zoneSigning,
            you must also provide one for the other.
          returned: success
          type: complex
          contains:
            algorithm:
              description:
              - String mnemonic specifying the DNSSEC algorithm of this key.
              returned: success
              type: str
            keyLength:
              description:
              - Length of the keys in bits.
              returned: success
              type: int
            keyType:
              description:
              - Specifies whether this is a key signing key (KSK) or a zone signing
                key (ZSK). Key signing keys have the Secure Entry Point flag set and,
                when active, will only be used to sign resource record sets of type
                DNSKEY. Zone signing keys do not have the Secure Entry Point flag
                set and will be used to sign all other types of resource record sets.
                .
              returned: success
              type: str
            kind:
              description:
              - Identifies what kind of resource this is.
              returned: success
              type: str
    id:
      description:
      - Unique identifier for the resource; defined by the server.
      returned: success
      type: int
    name:
      description:
      - User assigned name for this resource.
      - Must be unique within the project.
      returned: success
      type: str
    nameServers:
      description:
      - Delegate your managed_zone to these virtual name servers; defined by the server
        .
      returned: success
      type: list
    nameServerSet:
      description:
      - Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet
        is a set of DNS name servers that all host the same ManagedZones. Most users
        will leave this field unset.
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
      - A set of key/value label pairs to assign to this ManagedZone.
      returned: success
      type: dict
    visibility:
      description:
      - 'The zone''s visibility: public zones are exposed to the Internet, while private
        zones are visible only to Virtual Private Cloud resources.'
      - 'Must be one of: `public`, `private`.'
      returned: success
      type: str
    privateVisibilityConfig:
      description:
      - For privately visible zones, the set of Virtual Private Cloud resources that
        the zone is visible from.
      returned: success
      type: complex
      contains:
        networks:
          description:
          - The list of VPC networks that can see this zone.
          returned: success
          type: complex
          contains:
            networkUrl:
              description:
              - The fully qualified URL of the VPC network to bind to.
              - This should be formatted like `U(https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`)
                .
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
    module = GcpModule(argument_spec=dict(dns_name=dict(type='list', elements='str')))

    if module._name == 'gcp_dns_managed_zone_facts':
        module.deprecate("The 'gcp_dns_managed_zone_facts' module has been renamed to 'gcp_dns_managed_zone_info'", version='2.13')

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/ndev.clouddns.readwrite']

    items = fetch_list(module, collection(module), module.params['dns_name'])
    if items.get('managedZones'):
        items = items.get('managedZones')
    else:
        items = []
    return_value = {'resources': items}
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/dns/v1/projects/{project}/managedZones".format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'dns')
    response = auth.get(link, params={'dnsName': query})
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
