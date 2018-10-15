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
module: gcp_container_cluster_facts
description:
  - Gather facts for GCP Cluster
short_description: Gather facts for GCP Cluster
version_added: 2.8
author: Google Inc. (@googlecloudplatform)
requirements:
    - python >= 2.6
    - requests >= 2.18.4
    - google-auth >= 1.3.0
options:
    zone:
        description:
            - The zone where the cluster is deployed.
        required: true
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name:  a cluster facts
  gcp_container_cluster_facts:
      zone: us-central1-a
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
        name:
            description:
                - The name of this cluster. The name must be unique within this project and zone,
                  and can be up to 40 characters. Must be Lowercase letters, numbers, and hyphens
                  only. Must start with a letter. Must end with a number or a letter.
            returned: success
            type: str
        description:
            description:
                - An optional description of this cluster.
            returned: success
            type: str
        initialNodeCount:
            description:
                - The number of nodes to create in this cluster. You must ensure that your Compute
                  Engine resource quota is sufficient for this number of instances. You must also
                  have available firewall and routes quota. For requests, this field should only be
                  used in lieu of a "nodePool" object, since this configuration (along with the "nodeConfig")
                  will be used to create a "NodePool" object with an auto-generated name. Do not use
                  this and a nodePool at the same time.
            returned: success
            type: int
        nodeConfig:
            description:
                - Parameters used in creating the cluster's nodes.
                - For requests, this field should only be used in lieu of a "nodePool" object, since
                  this configuration (along with the "initialNodeCount") will be used to create a
                  "NodePool" object with an auto-generated name. Do not use this and a nodePool at
                  the same time. For responses, this field will be populated with the node configuration
                  of the first node pool. If unspecified, the defaults are used.
            returned: success
            type: complex
            contains:
                machineType:
                    description:
                        - The name of a Google Compute Engine machine type (e.g.
                        - n1-standard-1).  If unspecified, the default machine type is n1-standard-1.
                    returned: success
                    type: str
                diskSizeGb:
                    description:
                        - Size of the disk attached to each node, specified in GB. The smallest allowed disk
                          size is 10GB. If unspecified, the default disk size is 100GB.
                    returned: success
                    type: int
                oauthScopes:
                    description:
                        - The set of Google API scopes to be made available on all of the node VMs under the
                          "default" service account.
                        - 'The following scopes are recommended, but not required, and by default are not
                          included:  U(https://www.googleapis.com/auth/compute) is required for mounting persistent
                          storage on your nodes.'
                        - U(https://www.googleapis.com/auth/devstorage.read_only) is required for communicating
                          with gcr.io (the Google Container Registry).
                        - If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are
                          enabled, in which case their required scopes will be added.
                    returned: success
                    type: list
                serviceAccount:
                    description:
                        - The Google Cloud Platform Service Account to be used by the node VMs.  If no Service
                          Account is specified, the "default" service account is used.
                    returned: success
                    type: str
                metadata:
                    description:
                        - The metadata key/value pairs assigned to instances in the cluster.
                        - 'Keys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes in length.
                          These are reflected as part of a URL in the metadata server. Additionally, to avoid
                          ambiguity, keys must not conflict with any other metadata keys for the project or
                          be one of the four reserved keys: "instance-template", "kube-env", "startup-script",
                          and "user-data"  Values are free-form strings, and only have meaning as interpreted
                          by the image running in the instance. The only restriction placed on them is that
                          each value''s size must be less than or equal to 32 KB.'
                        - The total size of all keys and values must be less than 512 KB.
                        - 'An object containing a list of "key": value pairs.'
                        - 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'
                    returned: success
                    type: dict
                imageType:
                    description:
                        - The image type to use for this node.  Note that for a given image type, the latest
                          version of it will be used.
                    returned: success
                    type: str
                labels:
                    description:
                        - 'The map of Kubernetes labels (key/value pairs) to be applied to each node.
                          These will added in addition to any default label(s) that Kubernetes may apply
                          to the node. In case of conflict in label keys, the applied set may differ
                          depending on the Kubernetes version -- it''s best to assume the behavior is
                          undefined and conflicts should be avoided. For more information, including
                          usage and the valid values, see:
                          U(http://kubernetes.io/v1.1/docs/user-guide/labels.html) An object containing
                          a list of "key": value pairs.'
                        - 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'
                    returned: success
                    type: dict
                localSsdCount:
                    description:
                        - The number of local SSD disks to be attached to the node.
                        - 'The limit for this value is dependant upon the maximum number of disks available
                          on a machine per zone. See:  U(https://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits)  for
                          more information.'
                    returned: success
                    type: int
                tags:
                    description:
                        - The list of instance tags applied to all nodes. Tags are used to identify valid
                          sources or targets for network firewalls and are specified by the client during
                          cluster or node pool creation. Each tag within the list must comply with RFC1035.
                    returned: success
                    type: list
                preemptible:
                    description:
                        - 'Whether the nodes are created as preemptible VM instances. See: U(https://cloud.google.com/compute/docs/instances/preemptible)
                          for more inforamtion about preemptible VM instances.'
                    returned: success
                    type: bool
        masterAuth:
            description:
                - The authentication information for accessing the master endpoint.
            returned: success
            type: complex
            contains:
                username:
                    description:
                        - The username to use for HTTP basic authentication to the master endpoint.
                    returned: success
                    type: str
                password:
                    description:
                        - The password to use for HTTP basic authentication to the master endpoint. Because
                          the master endpoint is open to the Internet, you should create a strong password.
                    returned: success
                    type: str
                clusterCaCertificate:
                    description:
                        - Base64-encoded public certificate that is the root of trust for the cluster.
                    returned: success
                    type: str
                clientCertificate:
                    description:
                        - Base64-encoded public certificate used by clients to authenticate to the cluster
                          endpoint.
                    returned: success
                    type: str
                clientKey:
                    description:
                        - Base64-encoded private key used by clients to authenticate to the cluster endpoint.
                    returned: success
                    type: str
        loggingService:
            description:
                - 'The logging service the cluster should use to write logs. Currently available options:  logging.googleapis.com
                  - the Google Cloud Logging service.'
                - none - no logs will be exported from the cluster.
                - if left as an empty string,logging.googleapis.com will be used.
            returned: success
            type: str
        monitoringService:
            description:
                - The monitoring service the cluster should use to write metrics.
                - 'Currently available options:  monitoring.googleapis.com - the Google Cloud Monitoring
                  service.'
                - none - no metrics will be exported from the cluster.
                - if left as an empty string, monitoring.googleapis.com will be used.
            returned: success
            type: str
        network:
            description:
                - The name of the Google Compute Engine network to which the cluster is connected.
                  If left unspecified, the default network will be used.
                - To ensure it exists and it is operations, configure the network using 'gcompute_network'
                  resource.
            returned: success
            type: str
        clusterIpv4Cidr:
            description:
                - The IP address range of the container pods in this cluster, in CIDR notation (e.g.
                  10.96.0.0/14). Leave blank to have one automatically chosen or specify a /14 block
                  in 10.0.0.0/8.
            returned: success
            type: str
        addonsConfig:
            description:
                - Configurations for the various addons available to run in the cluster.
            returned: success
            type: complex
            contains:
                httpLoadBalancing:
                    description:
                        - Configuration for the HTTP (L7) load balancing controller addon, which makes it
                          easy to set up HTTP load balancers for services in a cluster.
                    returned: success
                    type: complex
                    contains:
                        disabled:
                            description:
                                - Whether the HTTP Load Balancing controller is enabled in the cluster. When enabled,
                                  it runs a small pod in the cluster that manages the load balancers.
                            returned: success
                            type: bool
                horizontalPodAutoscaling:
                    description:
                        - Configuration for the horizontal pod autoscaling feature, which increases or decreases
                          the number of replica pods a replication controller has based on the resource usage
                          of the existing pods.
                    returned: success
                    type: complex
                    contains:
                        disabled:
                            description:
                                - Whether the Horizontal Pod Autoscaling feature is enabled in the cluster. When enabled,
                                  it ensures that a Heapster pod is running in the cluster, which is also used by
                                  the Cloud Monitoring service.
                            returned: success
                            type: bool
        subnetwork:
            description:
                - The name of the Google Compute Engine subnetwork to which the cluster is connected.
            returned: success
            type: str
        location:
            description:
                - The list of Google Compute Engine locations in which the cluster's nodes should
                  be located.
            returned: success
            type: list
        endpoint:
            description:
                - The IP address of this cluster's master endpoint.
                - The endpoint can be accessed from the internet at https://username:password@endpoint/  See
                  the masterAuth property of this resource for username and password information.
            returned: success
            type: str
        initialClusterVersion:
            description:
                - The software version of the master endpoint and kubelets used in the cluster when
                  it was first created. The version can be upgraded over time.
            returned: success
            type: str
        currentMasterVersion:
            description:
                - The current software version of the master endpoint.
            returned: success
            type: str
        currentNodeVersion:
            description:
                - The current version of the node software components. If they are currently at multiple
                  versions because they're in the process of being upgraded, this reflects the minimum
                  version of all nodes.
            returned: success
            type: str
        createTime:
            description:
                - The time the cluster was created, in RFC3339 text format.
            returned: success
            type: str
        nodeIpv4CidrSize:
            description:
                - The size of the address space on each node for hosting containers.
                - This is provisioned from within the container_ipv4_cidr range.
            returned: success
            type: int
        servicesIpv4Cidr:
            description:
                - The IP address range of the Kubernetes services in this cluster, in CIDR notation
                  (e.g. 1.2.3.4/29). Service addresses are typically put in the last /16 from the
                  container CIDR.
            returned: success
            type: str
        currentNodeCount:
            description:
                - The number of nodes currently in the cluster.
            returned: success
            type: int
        expireTime:
            description:
                - The time the cluster will be automatically deleted in RFC3339 text format.
            returned: success
            type: str
        zone:
            description:
                - The zone where the cluster is deployed.
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
            zone=dict(required=True, type='str')
        )
    )

    if 'scopes' not in module.params:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    items = fetch_list(module, collection(module))
    if items.get('clusters'):
        items = items.get('clusters')
    else:
        items = []
    return_value = {
        'items': items
    }
    module.exit_json(**return_value)


def collection(module):
    return "https://container.googleapis.com/v1/projects/{project}/zones/{zone}/clusters".format(**module.params)


def fetch_list(module, link):
    auth = GcpSession(module, 'container')
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
