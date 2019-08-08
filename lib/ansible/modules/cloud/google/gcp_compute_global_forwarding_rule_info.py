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
module: gcp_compute_global_forwarding_rule_info
description:
- Gather info for GCP GlobalForwardingRule
- This module was called C(gcp_compute_global_forwarding_rule_facts) before Ansible
  2.9. The usage has not changed.
short_description: Gather info for GCP GlobalForwardingRule
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
- name: get info on a global forwarding rule
  gcp_compute_global_forwarding_rule_info:
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
    description:
      description:
      - An optional description of this resource. Provide this property when you create
        the resource.
      returned: success
      type: str
    id:
      description:
      - The unique identifier for the resource.
      returned: success
      type: int
    IPAddress:
      description:
      - The IP address that this forwarding rule is serving on behalf of.
      - Addresses are restricted based on the forwarding rule's load balancing scheme
        (EXTERNAL or INTERNAL) and scope (global or regional).
      - When the load balancing scheme is EXTERNAL, for global forwarding rules, the
        address must be a global IP, and for regional forwarding rules, the address
        must live in the same region as the forwarding rule. If this field is empty,
        an ephemeral IPv4 address from the same scope (global or regional) will be
        assigned. A regional forwarding rule supports IPv4 only. A global forwarding
        rule supports either IPv4 or IPv6.
      - When the load balancing scheme is INTERNAL, this can only be an RFC 1918 IP
        address belonging to the network/subnet configured for the forwarding rule.
        By default, if this field is empty, an ephemeral internal IP address will
        be automatically allocated from the IP range of the subnet or network configured
        for this forwarding rule.
      - 'An address can be specified either by a literal IP address or a URL reference
        to an existing Address resource. The following examples are all valid: * 100.1.2.3
        * U(https://www.googleapis.com/compute/v1/projects/project/regions/region/addresses/address)
        * projects/project/regions/region/addresses/address * regions/region/addresses/address
        * global/addresses/address * address .'
      returned: success
      type: str
    IPProtocol:
      description:
      - The IP protocol to which this rule applies. Valid options are TCP, UDP, ESP,
        AH, SCTP or ICMP. When the load balancing scheme is INTERNAL_SELF_MANAGED,
        only TCP is valid.
      returned: success
      type: str
    ipVersion:
      description:
      - The IP Version that will be used by this global forwarding rule.
      - Valid options are IPV4 or IPV6.
      returned: success
      type: str
    loadBalancingScheme:
      description:
      - This signifies what the GlobalForwardingRule will be used for.
      - 'The value of INTERNAL_SELF_MANAGED means that this will be used for Internal
        Global HTTP(S) LB. The value of EXTERNAL means that this will be used for
        External Global Load Balancing (HTTP(S) LB, External TCP/UDP LB, SSL Proxy)
        NOTE: Currently global forwarding rules cannot be used for INTERNAL load balancing.'
      returned: success
      type: str
    name:
      description:
      - Name of the resource; provided by the client when the resource is created.
        The name must be 1-63 characters long, and comply with RFC1035. Specifically,
        the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
        which means the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last character,
        which cannot be a dash.
      returned: success
      type: str
    network:
      description:
      - This field is not used for external load balancing.
      - For INTERNAL_SELF_MANAGED load balancing, this field identifies the network
        that the load balanced IP should belong to for this global forwarding rule.
        If this field is not specified, the default network will be used.
      returned: success
      type: dict
    portRange:
      description:
      - This field is used along with the target field for TargetHttpProxy, TargetHttpsProxy,
        TargetSslProxy, TargetTcpProxy, TargetVpnGateway, TargetPool, TargetInstance.
      - Applicable only when IPProtocol is TCP, UDP, or SCTP, only packets addressed
        to ports in the specified range will be forwarded to target.
      - Forwarding rules with the same [IPAddress, IPProtocol] pair must have disjoint
        port ranges.
      - 'Some types of forwarding target have constraints on the acceptable ports:
        * TargetHttpProxy: 80, 8080 * TargetHttpsProxy: 443 * TargetTcpProxy: 25,
        43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 * TargetSslProxy:
        25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 * TargetVpnGateway:
        500, 4500 .'
      returned: success
      type: str
    target:
      description:
      - The URL of the target resource to receive the matched traffic.
      - The forwarded traffic must be of a type appropriate to the target object.
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

    if module._name == 'gcp_compute_global_forwarding_rule_facts':
        module.deprecate("The 'gcp_compute_global_forwarding_rule_facts' module has been renamed to 'gcp_compute_global_forwarding_rule_info'", version='2.13')

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
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/forwardingRules".format(**module.params)


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
