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
module: gcp_mlengine_version_facts
description:
- Gather facts for GCP Version
short_description: Gather facts for GCP Version
version_added: 2.9
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  model:
    description:
    - The model that this version belongs to.
    - 'This field represents a link to a Model resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''name'' and value of
      your resource''s name Alternatively, you can add `register: name-of-resource`
      to a gcp_mlengine_model task and then set this model field to "{{ name-of-resource
      }}"'
    required: true
    type: dict
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: " a version facts"
  gcp_mlengine_version_facts:
    model: "{{ model }}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: facts
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    name:
      description:
      - The name specified for the version when it was created.
      - The version name must be unique within the model it is created in.
      returned: success
      type: str
    description:
      description:
      - The description specified for the version when it was created.
      returned: success
      type: str
    deploymentUri:
      description:
      - The Cloud Storage location of the trained model used to create the version.
      returned: success
      type: str
    createTime:
      description:
      - The time the version was created.
      returned: success
      type: str
    lastUseTime:
      description:
      - The time the version was last used for prediction.
      returned: success
      type: str
    runtimeVersion:
      description:
      - The AI Platform runtime version to use for this deployment.
      returned: success
      type: str
    machineType:
      description:
      - The type of machine on which to serve the model. Currently only applies to
        online prediction service.
      returned: success
      type: str
    state:
      description:
      - The state of a version.
      returned: success
      type: str
    errorMessage:
      description:
      - The details of a failure or cancellation.
      returned: success
      type: str
    packageUris:
      description:
      - Cloud Storage paths (gs://…) of packages for custom prediction routines or
        scikit-learn pipelines with custom code.
      returned: success
      type: list
    labels:
      description:
      - One or more labels that you can add, to organize your model versions.
      returned: success
      type: dict
    framework:
      description:
      - The machine learning framework AI Platform uses to train this version of the
        model.
      returned: success
      type: str
    pythonVersion:
      description:
      - The version of Python used in prediction. If not set, the default version
        is '2.7'. Python '3.5' is available when runtimeVersion is set to '1.4' and
        above. Python '2.7' works with all supported runtime versions.
      returned: success
      type: str
    serviceAccount:
      description:
      - Specifies the service account for resource access control.
      returned: success
      type: str
    autoScaling:
      description:
      - Automatically scale the number of nodes used to serve the model in response
        to increases and decreases in traffic. Care should be taken to ramp up traffic
        according to the model's ability to scale or you will start seeing increases
        in latency and 429 response codes.
      returned: success
      type: complex
      contains:
        minNodes:
          description:
          - The minimum number of nodes to allocate for this mode.
          returned: success
          type: int
    manualScaling:
      description:
      - Manually select the number of nodes to use for serving the model. You should
        generally use autoScaling with an appropriate minNodes instead, but this option
        is available if you want more predictable billing. Beware that latency and
        error rates will increase if the traffic exceeds that capability of the system
        to serve it based on the selected number of nodes.
      returned: success
      type: complex
      contains:
        nodes:
          description:
          - The number of nodes to allocate for this model. These nodes are always
            up, starting from the time the model is deployed.
          returned: success
          type: int
    predictionClass:
      description:
      - The fully qualified name (module_name.class_name) of a class that implements
        the Predictor interface described in this reference field. The module containing
        this class should be included in a package provided to the packageUris field.
      returned: success
      type: str
    model:
      description:
      - The model that this version belongs to.
      returned: success
      type: dict
    isDefault:
      description:
      - If true, this version will be used to handle prediction requests that do not
        specify a version.
      returned: success
      type: bool
'''

################################################################################
# Imports
################################################################################
from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict(model=dict(required=True, type='dict')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    items = fetch_list(module, collection(module))
    if items.get('versions'):
        items = items.get('versions')
    else:
        items = []
    return_value = {'resources': items}
    module.exit_json(**return_value)


def collection(module):
    res = {'project': module.params['project'], 'model': replace_resource_dict(module.params['model'], 'name')}
    return "https://ml.googleapis.com/v1/projects/{project}/models/{model}/versions".format(**res)


def fetch_list(module, link):
    auth = GcpSession(module, 'mlengine')
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
