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
module: gcp_storage_object
description:
- Upload or download a file from a GCS bucket.
short_description: Creates a GCP Object
version_added: 2.8
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
  action:
    description:
    - Upload or download from the bucket.
    - 'Some valid choices include: download, upload'
    required: false
  overwrite:
    description:
    - "'Overwrite the file on the bucket/local machine. If overwrite is false and
      a difference exists between GCS + local, module will fail with error' ."
    required: false
    type: bool
  src:
    description:
    - Source location of file (may be local machine or cloud depending on action).
    required: false
  dest:
    description:
    - Destination location of file (may be local machine or cloud depending on action).
    required: false
  bucket:
    description:
    - The name of the bucket.
    required: false
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: create a object
  gcp_storage_object:
    name: ansible-storage-module
    action: download
    bucket: ansible-bucket
    src: modules.zip
    dest: "~/modules.zip"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
action:
  description:
  - Upload or download from the bucket.
  returned: success
  type: str
overwrite:
  description:
  - "'Overwrite the file on the bucket/local machine. If overwrite is false and a
    difference exists between GCS + local, module will fail with error' ."
  returned: success
  type: bool
src:
  description:
  - Source location of file (may be local machine or cloud depending on action).
  returned: success
  type: str
dest:
  description:
  - Destination location of file (may be local machine or cloud depending on action).
  returned: success
  type: str
bucket:
  description:
  - The name of the bucket.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json
import os
import mimetypes
import hashlib
import base64

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            action=dict(type='str'),
            overwrite=dict(type='bool'),
            src=dict(type='path'),
            dest=dict(type='path'),
            bucket=dict(type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/devstorage.full_control']

    remote_object = fetch_resource(module, self_link(module))
    local_file_exists = os.path.isfile(local_file_path(module))

    # Check if files exist.
    if module.params['action'] == 'download' and not remote_object:
        module.fail_json(msg="File does not exist in bucket")

    if module.params['action'] == 'upload' and not local_file_exists:
        module.fail_json(msg="File does not exist on disk")

    # Check if we'll be overwriting files.
    if not module.params['overwrite']:
        remote_object['changed'] = False
        if module.params['action'] == 'download' and local_file_exists:
            # If files differ, throw an error
            if get_md5_local(local_file_path(module)) != remote_object['md5Hash']:
                module.fail_json(msg="Local file is different than remote file")
            # If files are the same, module is done running.
            else:
                module.exit_json(**remote_object)

        elif module.params['action'] == 'upload' and remote_object:
            # If files differ, throw an error
            if get_md5_local(local_file_path(module)) != remote_object['md5Hash']:
                module.fail_json(msg="Local file is different than remote file")
            # If files are the same, module is done running.
            else:
                module.exit_json(**remote_object)

    # Upload/download the files
    auth = GcpSession(module, 'storage')
    if module.params['action'] == 'download':
        results = download_file(module)
    else:
        results = upload_file(module)

    module.exit_json(**results)


def download_file(module):
    auth = GcpSession(module, 'storage')
    data = auth.get(media_link(module))
    with open(module.params['dest'], 'w') as f:
        f.write(data.text.encode('utf8'))
    return fetch_resource(module, self_link(module))


def upload_file(module):
    auth = GcpSession(module, 'storage')
    with open(module.params['src'], 'r') as f:
        results = return_if_object(module, auth.post_contents(upload_link(module), f, object_headers(module)))
    results['changed'] = True
    return results


def get_md5_local(path):
    md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
    return base64.b64encode(md5.digest())


def get_md5_remote(module):
    resource = fetch_resource(module, self_link(module))
    return resource.get('md5Hash')


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'storage')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    if module.params['action'] == 'download':
        return "https://www.googleapis.com/storage/v1/b/{bucket}/o/{src}".format(**module.params)
    else:
        return "https://www.googleapis.com/storage/v1/b/{bucket}/o/{dest}".format(**module.params)


def local_file_path(module):
    if module.params['action'] == 'download':
        return module.params['dest']
    else:
        return module.params['src']


def media_link(module):
    if module.params['action'] == 'download':
        return "https://www.googleapis.com/storage/v1/b/{bucket}/o/{src}?alt=media".format(**module.params)
    else:
        return "https://www.googleapis.com/storage/v1/b/{bucket}/o/{dest}?alt=media".format(**module.params)


def upload_link(module):
    return "https://www.googleapis.com/upload/storage/v1/b/{bucket}/o?uploadType=media&name={dest}".format(**module.params)


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
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def object_headers(module):
    return {
        "name": module.params['dest'],
        "Content-Type": mimetypes.guess_type(module.params['src'])[0],
        "Content-Length": str(os.path.getsize(module.params['src'])),
    }


if __name__ == '__main__':
    main()
