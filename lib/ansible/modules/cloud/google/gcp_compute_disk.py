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
module: gcp_compute_disk
description:
    - Persistent disks are durable storage devices that function similarly to the physical
      disks in a desktop or a server. Compute Engine manages the hardware behind these
      devices to ensure data redundancy and optimize performance for you. Persistent disks
      are available as either standard hard disk drives (HDD) or solid-state drives (SSD).
    - Persistent disks are located independently from your virtual machine instances,
      so you can detach or move persistent disks to keep your data even after you delete
      your instances. Persistent disk performance scales automatically with size, so you
      can resize your existing persistent disks or add more persistent disks to an instance
      to meet your performance and storage space requirements.
    - Add a persistent disk to your instance when you need reliable and affordable storage
      with consistent performance characteristics.
short_description: Creates a GCP Disk
version_added: 2.6
author: Google Inc. (@googlecloudplatform)
requirements:
    - python >= 2.6
    - requests >= 2.18.4
    - google-auth >= 1.3.0
options:
    state:
        description:
            - Whether the given object should exist in GCP
        choices: ['present', 'absent']
        default: 'present'
    description:
        description:
            - An optional description of this resource. Provide this property when you create
              the resource.
        required: false
    labels:
        description:
            - Labels to apply to this disk.  A list of key->value pairs.
        required: false
        version_added: 2.7
    licenses:
        description:
            - Any applicable publicly visible licenses.
        required: false
    name:
        description:
            - Name of the resource. Provided by the client when the resource is created. The name
              must be 1-63 characters long, and comply with RFC1035. Specifically, the name must
              be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
              which means the first character must be a lowercase letter, and all following characters
              must be a dash, lowercase letter, or digit, except the last character, which cannot
              be a dash.
        required: true
    size_gb:
        description:
            - Size of the persistent disk, specified in GB. You can specify this field when creating
              a persistent disk using the sourceImage or sourceSnapshot parameter, or specify
              it alone to create an empty persistent disk.
            - If you specify this field along with sourceImage or sourceSnapshot, the value of
              sizeGb must not be less than the size of the sourceImage or the size of the snapshot.
        required: false
    type:
        description:
            - URL of the disk type resource describing which disk type to use to create the disk.
              Provide this when creating the disk.
        required: false
        version_added: 2.7
    source_image:
        description:
            - The source image used to create this disk. If the source image is deleted, this
              field will not be set.
            - 'To create a disk with one of the public operating system images, specify the image
              by its family name. For example, specify family/debian-8 to use the latest Debian
              8 image:  projects/debian-cloud/global/images/family/debian-8  Alternatively, use
              a specific version of a public operating system image:  projects/debian-cloud/global/images/debian-8-jessie-vYYYYMMDD  To
              create a disk with a private image that you created, specify the image name in the
              following format:  global/images/my-private-image  You can also specify a private
              image by its image family, which returns the latest version of the image in that
              family. Replace the image name with family/family-name:  global/images/family/my-private-family
              .'
        required: false
    zone:
        description:
            - A reference to the zone where the disk resides.
        required: true
    source_image_encryption_key:
        description:
            - The customer-supplied encryption key of the source image. Required if the source
              image is protected by a customer-supplied encryption key.
        required: false
        suboptions:
            raw_key:
                description:
                    - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64
                      to either encrypt or decrypt this resource.
                required: false
            sha256:
                description:
                    - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key
                      that protects this resource.
                required: false
    disk_encryption_key:
        description:
            - Encrypts the disk using a customer-supplied encryption key.
            - After you encrypt a disk with a customer-supplied key, you must provide the same
              key if you use the disk later (e.g. to create a disk snapshot or an image, or to
              attach the disk to a virtual machine).
            - Customer-supplied encryption keys do not protect access to metadata of the disk.
            - If you do not provide an encryption key when creating the disk, then the disk will
              be encrypted using an automatically generated key and you do not need to provide
              a key to use the disk later.
        required: false
        suboptions:
            raw_key:
                description:
                    - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64
                      to either encrypt or decrypt this resource.
                required: false
            sha256:
                description:
                    - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key
                      that protects this resource.
                required: false
    source_snapshot:
        description:
            - 'The source snapshot used to create this disk. You can provide this as a partial or
              full URL to the resource. For example, the following are valid values: *
              `U(https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot`)
              * `projects/project/global/snapshots/snapshot` * `global/snapshots/snapshot` .'
        required: false
    source_snapshot_encryption_key:
        description:
            - The customer-supplied encryption key of the source snapshot. Required if the source
              snapshot is protected by a customer-supplied encryption key.
        required: false
        suboptions:
            raw_key:
                description:
                    - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64
                      to either encrypt or decrypt this resource.
                required: false
            sha256:
                description:
                    - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key
                      that protects this resource.
                required: false
extends_documentation_fragment: gcp
notes:
    - "API Reference: U(https://cloud.google.com/compute/docs/reference/latest/disks)"
    - "Adding a persistent disk: U(https://cloud.google.com/compute/docs/disks/add-persistent-disk)"
'''

EXAMPLES = '''
- name: create a disk
  gcp_compute_disk:
      name: "test_object"
      size_gb: 50
      disk_encryption_key:
        raw_key: SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=
      zone: us-central1-a
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present
'''

RETURN = '''
    creation_timestamp:
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
    last_attach_timestamp:
        description:
            - Last attach timestamp in RFC3339 text format.
        returned: success
        type: str
    last_detach_timestamp:
        description:
            - Last dettach timestamp in RFC3339 text format.
        returned: success
        type: str
    labels:
        description:
            - Labels to apply to this disk.  A list of key->value pairs.
        returned: success
        type: dict
    licenses:
        description:
            - Any applicable publicly visible licenses.
        returned: success
        type: list
    name:
        description:
            - Name of the resource. Provided by the client when the resource is created. The name
              must be 1-63 characters long, and comply with RFC1035. Specifically, the name must
              be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
              which means the first character must be a lowercase letter, and all following characters
              must be a dash, lowercase letter, or digit, except the last character, which cannot
              be a dash.
        returned: success
        type: str
    size_gb:
        description:
            - Size of the persistent disk, specified in GB. You can specify this field when creating
              a persistent disk using the sourceImage or sourceSnapshot parameter, or specify
              it alone to create an empty persistent disk.
            - If you specify this field along with sourceImage or sourceSnapshot, the value of
              sizeGb must not be less than the size of the sourceImage or the size of the snapshot.
        returned: success
        type: int
    type:
        description:
            - URL of the disk type resource describing which disk type to use to create the disk.
              Provide this when creating the disk.
        returned: success
        type: str
    users:
        description:
            - 'Links to the users of the disk (attached instances) in form: project/zones/zone/instances/instance
              .'
        returned: success
        type: list
    source_image:
        description:
            - The source image used to create this disk. If the source image is deleted, this
              field will not be set.
            - 'To create a disk with one of the public operating system images, specify the image
              by its family name. For example, specify family/debian-8 to use the latest Debian
              8 image:  projects/debian-cloud/global/images/family/debian-8  Alternatively, use
              a specific version of a public operating system image:  projects/debian-cloud/global/images/debian-8-jessie-vYYYYMMDD  To
              create a disk with a private image that you created, specify the image name in the
              following format:  global/images/my-private-image  You can also specify a private
              image by its image family, which returns the latest version of the image in that
              family. Replace the image name with family/family-name:  global/images/family/my-private-family
              .'
        returned: success
        type: str
    zone:
        description:
            - A reference to the zone where the disk resides.
        returned: success
        type: str
    source_image_encryption_key:
        description:
            - The customer-supplied encryption key of the source image. Required if the source
              image is protected by a customer-supplied encryption key.
        returned: success
        type: complex
        contains:
            raw_key:
                description:
                    - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64
                      to either encrypt or decrypt this resource.
                returned: success
                type: str
            sha256:
                description:
                    - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key
                      that protects this resource.
                returned: success
                type: str
    source_image_id:
        description:
            - The ID value of the image used to create this disk. This value identifies the exact
              image that was used to create this persistent disk. For example, if you created
              the persistent disk from an image that was later deleted and recreated under the
              same name, the source image ID would identify the exact version of the image that
              was used.
        returned: success
        type: str
    disk_encryption_key:
        description:
            - Encrypts the disk using a customer-supplied encryption key.
            - After you encrypt a disk with a customer-supplied key, you must provide the same
              key if you use the disk later (e.g. to create a disk snapshot or an image, or to
              attach the disk to a virtual machine).
            - Customer-supplied encryption keys do not protect access to metadata of the disk.
            - If you do not provide an encryption key when creating the disk, then the disk will
              be encrypted using an automatically generated key and you do not need to provide
              a key to use the disk later.
        returned: success
        type: complex
        contains:
            raw_key:
                description:
                    - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64
                      to either encrypt or decrypt this resource.
                returned: success
                type: str
            sha256:
                description:
                    - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key
                      that protects this resource.
                returned: success
                type: str
    source_snapshot:
        description:
            - 'The source snapshot used to create this disk. You can provide this as a partial or
              full URL to the resource. For example, the following are valid values: *
              `U(https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot`)
              * `projects/project/global/snapshots/snapshot` * `global/snapshots/snapshot` .'
        returned: success
        type: dict
    source_snapshot_encryption_key:
        description:
            - The customer-supplied encryption key of the source snapshot. Required if the source
              snapshot is protected by a customer-supplied encryption key.
        returned: success
        type: complex
        contains:
            raw_key:
                description:
                    - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64
                      to either encrypt or decrypt this resource.
                returned: success
                type: str
            sha256:
                description:
                    - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption key
                      that protects this resource.
                returned: success
                type: str
    source_snapshot_id:
        description:
            - The unique ID of the snapshot used to create this disk. This value identifies the
              exact snapshot that was used to create this persistent disk. For example, if you
              created the persistent disk from a snapshot that was later deleted and recreated
              under the same name, the source snapshot ID would identify the exact version of
              the snapshot that was used.
        returned: success
        type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import re
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            description=dict(type='str'),
            labels=dict(type='dict'),
            licenses=dict(type='list', elements='str'),
            name=dict(required=True, type='str'),
            size_gb=dict(type='int'),
            type=dict(type='str'),
            source_image=dict(type='str'),
            zone=dict(required=True, type='str'),
            source_image_encryption_key=dict(type='dict', options=dict(
                raw_key=dict(type='str'),
                sha256=dict(type='str')
            )),
            disk_encryption_key=dict(type='dict', options=dict(
                raw_key=dict(type='str'),
                sha256=dict(type='str')
            )),
            source_snapshot=dict(type='dict'),
            source_snapshot_encryption_key=dict(type='dict', options=dict(
                raw_key=dict(type='str'),
                sha256=dict(type='str')
            ))
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#disk'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update_fields(module, resource_to_request(module),
                              response_to_hash(module, fetch))
                fetch = update(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.put(link, resource_to_request(module)))


def update_fields(module, request, response):
    difference = GcpRequest(request).difference(GcpRequest(response))
    auth = GcpSession(module, 'compute')
    if difference.get('labels'):
        auth.post(
            ''.join([
                "https://www.googleapis.com/compute/v1/",
                "projects/{project}/zones/{zone}/disks/{name}/setLabels"
            ]).format(**module.params),
            {
                u'labels': module.params.get('labels')
            }
        )
    if difference.get('size_gb'):
        auth.post(
            ''.join([
                "https://www.googleapis.com/compute/v1/",
                "projects/{project}/zones/{zone}/disks/{name}/resize"
            ]).format(**module.params),
            {
                u'sizeGb': module.params.get('size_gb')
            }
        )


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#disk',
        u'sourceImageEncryptionKey': DiskSourceImageEncryptionKey(module.params.get('source_image_encryption_key', {}), module).to_request(),
        u'diskEncryptionKey': DiskDiskEncryptionKey(module.params.get('disk_encryption_key', {}), module).to_request(),
        u'sourceSnapshotEncryptionKey': DiskSourceSnapshotEncryptionKey(module.params.get('source_snapshot_encryption_key', {}), module).to_request(),
        u'description': module.params.get('description'),
        u'labels': module.params.get('labels'),
        u'licenses': module.params.get('licenses'),
        u'name': module.params.get('name'),
        u'sizeGb': module.params.get('size_gb'),
        u'type': disk_type_selflink(module.params.get('type'), module.params),
        u'sourceImage': module.params.get('source_image')
    }
    return_vals = {}
    for k, v in request.items():
        if v:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/disks/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/disks".format(**module.params)


def return_if_object(module, response, kind):
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
    if result['kind'] != kind:
        module.fail_json(msg="Incorrect result: {kind}".format(**result))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

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
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'id': response.get(u'id'),
        u'lastAttachTimestamp': response.get(u'lastAttachTimestamp'),
        u'lastDetachTimestamp': response.get(u'lastDetachTimestamp'),
        u'labels': response.get(u'labels'),
        u'licenses': response.get(u'licenses'),
        u'name': module.params.get('name'),
        u'sizeGb': response.get(u'sizeGb'),
        u'type': response.get(u'type'),
        u'users': response.get(u'users'),
        u'sourceImage': module.params.get('source_image')
    }


def disk_type_selflink(name, params):
    if name is None:
        return
    url = r"https://www.googleapis.com/compute/v1/projects/.*/zones/{zone}/diskTypes/[a-z1-9\-]*"
    if not re.match(url, name):
        name = "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/diskTypes/%s".format(**params) % name
    return name


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#disk')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], 'message')
        time.sleep(1.0)
        if status not in ['PENDING', 'RUNNING', 'DONE']:
            module.fail_json(msg="Invalid result %s" % status)
        op_result = fetch_resource(module, op_uri, 'compute#operation')
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class DiskSourceImageEncryptionKey(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({
            u'rawKey': self.request.get('raw_key'),
            u'sha256': self.request.get('sha256')
        })

    def from_response(self):
        return remove_nones_from_dict({
            u'rawKey': self.request.get(u'rawKey'),
            u'sha256': self.request.get(u'sha256')
        })


class DiskDiskEncryptionKey(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({
            u'rawKey': self.request.get('raw_key'),
            u'sha256': self.request.get('sha256')
        })

    def from_response(self):
        return remove_nones_from_dict({
            u'rawKey': self.request.get(u'rawKey'),
            u'sha256': self.request.get(u'sha256')
        })


class DiskSourceSnapshotEncryptionKey(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({
            u'rawKey': self.request.get('raw_key'),
            u'sha256': self.request.get('sha256')
        })

    def from_response(self):
        return remove_nones_from_dict({
            u'rawKey': self.request.get(u'rawKey'),
            u'sha256': self.request.get(u'sha256')
        })


if __name__ == '__main__':
    main()
