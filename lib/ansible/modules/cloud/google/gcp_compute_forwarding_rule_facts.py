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
module: gcp_compute_forwarding_rule_facts
description:
- Gather facts for GCP ForwardingRule
short_description: Gather facts for GCP ForwardingRule
version_added: 2.7
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  filters:
    description:
    - A list of filter value pairs. Available filters are listed here U(U(https://cloud.google.com/sdk/gcloud/reference/topic/filters).)
    - Each additional filter in the list will act be added as an AND condition (filter1
      and filter2) .
  region:
    description:
    - A reference to the region where the regional forwarding rule resides.
    - This field is not applicable to global forwarding rules.
    required: true
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name:  a forwarding rule facts
  gcp_compute_forwarding_rule_facts:
      region: us-west1
      filters:
      - name = test_object
      project: test_project
      auth_kind: serviceaccount
      service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
items:
  description: List of items
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
        AH, SCTP or ICMP.
      - When the load balancing scheme is INTERNAL, only TCP and UDP are valid.
      returned: success
      type: str
    backendService:
      description:
      - A reference to a BackendService to receive the matched traffic.
      - This is used for internal load balancing.
      - "(not used for external load balancing) ."
      returned: success
      type: dict
    ipVersion:
      description:
      - The IP Version that will be used by this forwarding rule. Valid options are
        IPV4 or IPV6. This can only be specified for a global forwarding rule.
      returned: success
      type: str
    loadBalancingScheme:
      description:
      - 'This signifies what the ForwardingRule will be used for and can only take
        the following values: INTERNAL, EXTERNAL The value of INTERNAL means that
        this will be used for Internal Network Load Balancing (TCP, UDP). The value
        of EXTERNAL means that this will be used for External Load Balancing (HTTP(S)
        LB, External TCP/UDP LB, SSL Proxy) .'
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
      - For internal load balancing, this field identifies the network that the load
        balanced IP should belong to for this Forwarding Rule. If this field is not
        specified, the default network will be used.
      - This field is not used for external load balancing.
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
    ports:
      description:
      - This field is used along with the backend_service field for internal load
        balancing.
      - When the load balancing scheme is INTERNAL, a single port or a comma separated
        list of ports can be configured. Only packets addressed to these ports will
        be forwarded to the backends configured with this forwarding rule.
      - You may specify a maximum of up to 5 ports.
      returned: success
      type: list
    subnetwork:
      description:
      - A reference to a subnetwork.
      - For internal load balancing, this field identifies the subnetwork that the
        load balanced IP should belong to for this Forwarding Rule.
      - If the network specified is in auto subnet mode, this field is optional. However,
        if the network is in custom subnet mode, a subnetwork must be specified.
      - This field is not used for external load balancing.
      returned: success
      type: dict
    target:
      description:
      - A reference to a TargetPool resource to receive the matched traffic.
      - For regional forwarding rules, this target must live in the same region as
        the forwarding rule. For global forwarding rules, this target must be a global
        load balancing resource. The forwarded traffic must be of a type appropriate
        to the target object.
      - This field is not used for internal load balancing.
      returned: success
      type: dict
    networkTier:
      description:
      - 'The networking tier used for configuring this address. This field can take
        the following values: PREMIUM or STANDARD. If this field is not specified,
        it is assumed to be PREMIUM.'
      returned: success
      type: str
    region:
      description:
      - A reference to the region where the regional forwarding rule resides.
      - This field is not applicable to global forwarding rules.
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
    module = GcpModule(
        argument_spec=dict(
            filters=dict(type='list', elements='str'),
            region=dict(required=True, type='str')
        )
    )

    if 'scopes' not in module.params:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

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
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/forwardingRules".format(**module.params)


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
