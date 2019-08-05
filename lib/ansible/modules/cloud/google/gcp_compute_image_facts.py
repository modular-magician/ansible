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
module: gcp_compute_image_facts
description:
- Gather facts for GCP Image
short_description: Gather facts for GCP Image
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
- name: " a image facts"
  gcp_compute_image_facts:
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
    archiveSizeBytes:
      description:
      - Size of the image tar.gz archive stored in Google Cloud Storage (in bytes).
      returned: success
      type: int
    creationTimestamp:
      description:
      - Creation timestamp in RFC3339 text format.
      returned: success
      type: str
    deprecated:
      description:
      - The deprecation status associated with this image.
      returned: success
      type: complex
      contains:
        deleted:
          description:
          - An optional RFC3339 timestamp on or after which the state of this resource
            is intended to change to DELETED. This is only informational and the status
            will not change unless the client explicitly changes it.
          returned: success
          type: str
        deprecated:
          description:
          - An optional RFC3339 timestamp on or after which the state of this resource
            is intended to change to DEPRECATED. This is only informational and the
            status will not change unless the client explicitly changes it.
          returned: success
          type: str
        obsolete:
          description:
          - An optional RFC3339 timestamp on or after which the state of this resource
            is intended to change to OBSOLETE. This is only informational and the
            status will not change unless the client explicitly changes it.
          returned: success
          type: str
        replacement:
          description:
          - The URL of the suggested replacement for a deprecated resource.
          - The suggested replacement resource must be the same kind of resource as
            the deprecated resource.
          returned: success
          type: str
        state:
          description:
          - The deprecation state of this resource. This can be DEPRECATED, OBSOLETE,
            or DELETED. Operations which create a new resource using a DEPRECATED
            resource will return successfully, but with a warning indicating the deprecated
            resource and recommending its replacement. Operations which use OBSOLETE
            or DELETED resources will be rejected and result in an error.
          returned: success
          type: str
    description:
      description:
      - An optional description of this resource. Provide this property when you create
        the resource.
      returned: success
      type: str
    diskSizeGb:
      description:
      - Size of the image when restored onto a persistent disk (in GB).
      returned: success
      type: int
    family:
      description:
      - The name of the image family to which this image belongs. You can create disks
        by specifying an image family instead of a specific image name. The image
        family always returns its latest image that is not deprecated. The name of
        the image family must comply with RFC1035.
      returned: success
      type: str
    guestOsFeatures:
      description:
      - A list of features to enable on the guest OS. Applicable for bootable images
        only. Currently, only one feature can be enabled, VIRTIO_SCSI_MULTIQUEUE,
        which allows each virtual CPU to have its own queue. For Windows images, you
        can only enable VIRTIO_SCSI_MULTIQUEUE on images with driver version 1.2.0.1621
        or higher. Linux images with kernel versions 3.17 and higher will support
        VIRTIO_SCSI_MULTIQUEUE.
      - For new Windows images, the server might also populate this field with the
        value WINDOWS, to indicate that this is a Windows image.
      - This value is purely informational and does not enable or disable any features.
      returned: success
      type: complex
      contains:
        type:
          description:
          - The type of supported feature. Currenty only VIRTIO_SCSI_MULTIQUEUE is
            supported. For newer Windows images, the server might also populate this
            property with the value WINDOWS to indicate that this is a Windows image.
            This value is purely informational and does not enable or disable any
            features.
          returned: success
          type: str
    id:
      description:
      - The unique identifier for the resource. This identifier is defined by the
        server.
      returned: success
      type: int
    imageEncryptionKey:
      description:
      - Encrypts the image using a customer-supplied encryption key.
      - After you encrypt an image with a customer-supplied key, you must provide
        the same key if you use the image later (e.g. to create a disk from the image)
        .
      returned: success
      type: complex
      contains:
        rawKey:
          description:
          - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648
            base64 to either encrypt or decrypt this resource.
          returned: success
          type: str
        sha256:
          description:
          - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption
            key that protects this resource.
          returned: success
          type: str
    labels:
      description:
      - Labels to apply to this Image.
      returned: success
      type: dict
    labelFingerprint:
      description:
      - The fingerprint used for optimistic locking of this resource. Used internally
        during updates.
      returned: success
      type: str
    licenses:
      description:
      - Any applicable license URI.
      returned: success
      type: list
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
    rawDisk:
      description:
      - The parameters of the raw disk image.
      returned: success
      type: complex
      contains:
        containerType:
          description:
          - The format used to encode and transmit the block device, which should
            be TAR. This is just a container and transmission format and not a runtime
            format. Provided by the client when the disk image is created.
          returned: success
          type: str
        sha1Checksum:
          description:
          - An optional SHA1 checksum of the disk image before unpackaging.
          - This is provided by the client when the disk image is created.
          returned: success
          type: str
        source:
          description:
          - The full Google Cloud Storage URL where disk storage is stored You must
            provide either this property or the sourceDisk property but not both.
          returned: success
          type: str
    sourceDisk:
      description:
      - The source disk to create this image based on.
      - You must provide either this property or the rawDisk.source property but not
        both to create an image.
      returned: success
      type: dict
    sourceDiskEncryptionKey:
      description:
      - The customer-supplied encryption key of the source disk. Required if the source
        disk is protected by a customer-supplied encryption key.
      returned: success
      type: complex
      contains:
        rawKey:
          description:
          - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648
            base64 to either encrypt or decrypt this resource.
          returned: success
          type: str
        sha256:
          description:
          - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption
            key that protects this resource.
          returned: success
          type: str
    sourceDiskId:
      description:
      - The ID value of the disk used to create this image. This value may be used
        to determine whether the image was taken from the current or a previous instance
        of a given disk name.
      returned: success
      type: str
    sourceType:
      description:
      - The type of the image used to create this disk. The default and only value
        is RAW .
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
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/images".format(**module.params)


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
