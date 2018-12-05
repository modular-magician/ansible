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
module: gcp_compute_health_check
description:
- Health Checks determine whether instances are responsive and able to do work.
- They are an important part of a comprehensive load balancing configuration, as they
  enable monitoring instances behind load balancers.
- Health Checks poll instances at a specified interval. Instances that do not respond
  successfully to some number of probes in a row are marked as unhealthy. No new connections
  are sent to unhealthy instances, though existing connections will continue. The
  health check will continue to poll unhealthy instances. If an instance later responds
  successfully to some number of consecutive probes, it is marked healthy again and
  can receive new connections.
short_description: Creates a GCP HealthCheck
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
    choices:
    - present
    - absent
    default: present
  check_interval_sec:
    description:
    - How often (in seconds) to send a health check. The default value is 5 seconds.
    required: false
    default: '5'
  description:
    description:
    - An optional description of this resource. Provide this property when you create
      the resource.
    required: false
  healthy_threshold:
    description:
    - A so-far unhealthy instance will be marked healthy after this many consecutive
      successes. The default value is 2.
    required: false
    default: '2'
  name:
    description:
    - Name of the resource. Provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
  timeout_sec:
    description:
    - How long (in seconds) to wait before claiming failure.
    - The default value is 5 seconds. It is invalid for timeoutSec to have greater
      value than checkIntervalSec.
    required: false
    default: '5'
    aliases:
    - timeout_seconds
  unhealthy_threshold:
    description:
    - A so-far healthy instance will be marked unhealthy after this many consecutive
      failures. The default value is 2.
    required: false
    default: '2'
  type:
    description:
    - Specifies the type of the healthCheck, either TCP, SSL, HTTP or HTTPS. If not
      specified, the default is TCP. Exactly one of the protocol-specific health check
      field must be specified, which must match type field.
    required: false
    choices:
    - TCP
    - SSL
    - HTTP
    - HTTPS
  http_health_check:
    description:
    - A nested object resource.
    required: false
    suboptions:
      host:
        description:
        - The value of the host header in the HTTP health check request.
        - If left empty (default value), the public IP on behalf of which this health
          check is performed will be used.
        required: false
      request_path:
        description:
        - The request path of the HTTP health check request.
        - The default value is /.
        required: false
        default: "/"
      response:
        description:
        - The bytes to match against the beginning of the response data. If left empty
          (the default value), any response will indicate health. The response data
          can only be ASCII.
        required: false
      port:
        description:
        - The TCP port number for the HTTP health check request.
        - The default value is 80.
        required: false
      port_name:
        description:
        - Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name
          are defined, port takes precedence.
        required: false
      proxy_header:
        description:
        - Specifies the type of proxy header to append before sending data to the
          backend, either NONE or PROXY_V1. The default is NONE.
        required: false
        default: NONE
        choices:
        - NONE
        - PROXY_V1
  https_health_check:
    description:
    - A nested object resource.
    required: false
    suboptions:
      host:
        description:
        - The value of the host header in the HTTPS health check request.
        - If left empty (default value), the public IP on behalf of which this health
          check is performed will be used.
        required: false
      request_path:
        description:
        - The request path of the HTTPS health check request.
        - The default value is /.
        required: false
        default: "/"
      response:
        description:
        - The bytes to match against the beginning of the response data. If left empty
          (the default value), any response will indicate health. The response data
          can only be ASCII.
        required: false
      port:
        description:
        - The TCP port number for the HTTPS health check request.
        - The default value is 443.
        required: false
      port_name:
        description:
        - Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name
          are defined, port takes precedence.
        required: false
      proxy_header:
        description:
        - Specifies the type of proxy header to append before sending data to the
          backend, either NONE or PROXY_V1. The default is NONE.
        required: false
        default: NONE
        choices:
        - NONE
        - PROXY_V1
  tcp_health_check:
    description:
    - A nested object resource.
    required: false
    suboptions:
      request:
        description:
        - The application data to send once the TCP connection has been established
          (default value is empty). If both request and response are empty, the connection
          establishment alone will indicate health. The request data can only be ASCII.
        required: false
      response:
        description:
        - The bytes to match against the beginning of the response data. If left empty
          (the default value), any response will indicate health. The response data
          can only be ASCII.
        required: false
      port:
        description:
        - The TCP port number for the TCP health check request.
        - The default value is 443.
        required: false
      port_name:
        description:
        - Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name
          are defined, port takes precedence.
        required: false
      proxy_header:
        description:
        - Specifies the type of proxy header to append before sending data to the
          backend, either NONE or PROXY_V1. The default is NONE.
        required: false
        default: NONE
        choices:
        - NONE
        - PROXY_V1
  ssl_health_check:
    description:
    - A nested object resource.
    required: false
    suboptions:
      request:
        description:
        - The application data to send once the SSL connection has been established
          (default value is empty). If both request and response are empty, the connection
          establishment alone will indicate health. The request data can only be ASCII.
        required: false
      response:
        description:
        - The bytes to match against the beginning of the response data. If left empty
          (the default value), any response will indicate health. The response data
          can only be ASCII.
        required: false
      port:
        description:
        - The TCP port number for the SSL health check request.
        - The default value is 443.
        required: false
      port_name:
        description:
        - Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name
          are defined, port takes precedence.
        required: false
      proxy_header:
        description:
        - Specifies the type of proxy header to append before sending data to the
          backend, either NONE or PROXY_V1. The default is NONE.
        required: false
        default: NONE
        choices:
        - NONE
        - PROXY_V1
extends_documentation_fragment: gcp
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/rest/latest/healthChecks)'
- 'Official Documentation: U(https://cloud.google.com/load-balancing/docs/health-checks)'
'''

EXAMPLES = '''
- name: create a health check
  gcp_compute_health_check:
      name: "test_object"
      type: TCP
      tcp_health_check:
        port_name: service-health
        request: ping
        response: pong
      healthy_threshold: 10
      timeout_sec: 2
      unhealthy_threshold: 5
      project: "test_project"
      auth_kind: "serviceaccount"
      service_account_file: "/tmp/auth.pem"
      state: present
'''

RETURN = '''
checkIntervalSec:
  description:
  - How often (in seconds) to send a health check. The default value is 5 seconds.
  returned: success
  type: int
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
healthyThreshold:
  description:
  - A so-far unhealthy instance will be marked healthy after this many consecutive
    successes. The default value is 2.
  returned: success
  type: int
id:
  description:
  - The unique identifier for the resource. This identifier is defined by the server.
  returned: success
  type: int
name:
  description:
  - Name of the resource. Provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
timeoutSec:
  description:
  - How long (in seconds) to wait before claiming failure.
  - The default value is 5 seconds. It is invalid for timeoutSec to have greater value
    than checkIntervalSec.
  returned: success
  type: int
unhealthyThreshold:
  description:
  - A so-far healthy instance will be marked unhealthy after this many consecutive
    failures. The default value is 2.
  returned: success
  type: int
type:
  description:
  - Specifies the type of the healthCheck, either TCP, SSL, HTTP or HTTPS. If not
    specified, the default is TCP. Exactly one of the protocol-specific health check
    field must be specified, which must match type field.
  returned: success
  type: str
httpHealthCheck:
  description:
  - A nested object resource.
  returned: success
  type: complex
  contains:
    host:
      description:
      - The value of the host header in the HTTP health check request.
      - If left empty (default value), the public IP on behalf of which this health
        check is performed will be used.
      returned: success
      type: str
    requestPath:
      description:
      - The request path of the HTTP health check request.
      - The default value is /.
      returned: success
      type: str
    response:
      description:
      - The bytes to match against the beginning of the response data. If left empty
        (the default value), any response will indicate health. The response data
        can only be ASCII.
      returned: success
      type: str
    port:
      description:
      - The TCP port number for the HTTP health check request.
      - The default value is 80.
      returned: success
      type: int
    portName:
      description:
      - Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name
        are defined, port takes precedence.
      returned: success
      type: str
    proxyHeader:
      description:
      - Specifies the type of proxy header to append before sending data to the backend,
        either NONE or PROXY_V1. The default is NONE.
      returned: success
      type: str
httpsHealthCheck:
  description:
  - A nested object resource.
  returned: success
  type: complex
  contains:
    host:
      description:
      - The value of the host header in the HTTPS health check request.
      - If left empty (default value), the public IP on behalf of which this health
        check is performed will be used.
      returned: success
      type: str
    requestPath:
      description:
      - The request path of the HTTPS health check request.
      - The default value is /.
      returned: success
      type: str
    response:
      description:
      - The bytes to match against the beginning of the response data. If left empty
        (the default value), any response will indicate health. The response data
        can only be ASCII.
      returned: success
      type: str
    port:
      description:
      - The TCP port number for the HTTPS health check request.
      - The default value is 443.
      returned: success
      type: int
    portName:
      description:
      - Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name
        are defined, port takes precedence.
      returned: success
      type: str
    proxyHeader:
      description:
      - Specifies the type of proxy header to append before sending data to the backend,
        either NONE or PROXY_V1. The default is NONE.
      returned: success
      type: str
tcpHealthCheck:
  description:
  - A nested object resource.
  returned: success
  type: complex
  contains:
    request:
      description:
      - The application data to send once the TCP connection has been established
        (default value is empty). If both request and response are empty, the connection
        establishment alone will indicate health. The request data can only be ASCII.
      returned: success
      type: str
    response:
      description:
      - The bytes to match against the beginning of the response data. If left empty
        (the default value), any response will indicate health. The response data
        can only be ASCII.
      returned: success
      type: str
    port:
      description:
      - The TCP port number for the TCP health check request.
      - The default value is 443.
      returned: success
      type: int
    portName:
      description:
      - Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name
        are defined, port takes precedence.
      returned: success
      type: str
    proxyHeader:
      description:
      - Specifies the type of proxy header to append before sending data to the backend,
        either NONE or PROXY_V1. The default is NONE.
      returned: success
      type: str
sslHealthCheck:
  description:
  - A nested object resource.
  returned: success
  type: complex
  contains:
    request:
      description:
      - The application data to send once the SSL connection has been established
        (default value is empty). If both request and response are empty, the connection
        establishment alone will indicate health. The request data can only be ASCII.
      returned: success
      type: str
    response:
      description:
      - The bytes to match against the beginning of the response data. If left empty
        (the default value), any response will indicate health. The response data
        can only be ASCII.
      returned: success
      type: str
    port:
      description:
      - The TCP port number for the SSL health check request.
      - The default value is 443.
      returned: success
      type: int
    portName:
      description:
      - Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name
        are defined, port takes precedence.
      returned: success
      type: str
    proxyHeader:
      description:
      - Specifies the type of proxy header to append before sending data to the backend,
        either NONE or PROXY_V1. The default is NONE.
      returned: success
      type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            check_interval_sec=dict(default=5, type='int'),
            description=dict(type='str'),
            healthy_threshold=dict(default=2, type='int'),
            name=dict(required=True, type='str'),
            timeout_sec=dict(default=5, type='int', aliases=['timeout_seconds']),
            unhealthy_threshold=dict(default=2, type='int'),
            type=dict(type='str', choices=['TCP', 'SSL', 'HTTP', 'HTTPS']),
            http_health_check=dict(type='dict', options=dict(
                host=dict(type='str'),
                request_path=dict(default='/', type='str'),
                response=dict(type='str'),
                port=dict(type='int'),
                port_name=dict(type='str'),
                proxy_header=dict(default='NONE', type='str', choices=['NONE', 'PROXY_V1'])
            )),
            https_health_check=dict(type='dict', options=dict(
                host=dict(type='str'),
                request_path=dict(default='/', type='str'),
                response=dict(type='str'),
                port=dict(type='int'),
                port_name=dict(type='str'),
                proxy_header=dict(default='NONE', type='str', choices=['NONE', 'PROXY_V1'])
            )),
            tcp_health_check=dict(type='dict', options=dict(
                request=dict(type='str'),
                response=dict(type='str'),
                port=dict(type='int'),
                port_name=dict(type='str'),
                proxy_header=dict(default='NONE', type='str', choices=['NONE', 'PROXY_V1'])
            )),
            ssl_health_check=dict(type='dict', options=dict(
                request=dict(type='str'),
                response=dict(type='str'),
                port=dict(type='int'),
                port_name=dict(type='str'),
                proxy_header=dict(default='NONE', type='str', choices=['NONE', 'PROXY_V1'])
            ))
        ),
        mutually_exclusive=[['http_health_check', 'https_health_check', 'ssl_health_check', 'tcp_health_check']]
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#healthCheck'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
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


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#healthCheck',
        u'checkIntervalSec': module.params.get('check_interval_sec'),
        u'description': module.params.get('description'),
        u'healthyThreshold': module.params.get('healthy_threshold'),
        u'name': module.params.get('name'),
        u'timeoutSec': module.params.get('timeout_sec'),
        u'unhealthyThreshold': module.params.get('unhealthy_threshold'),
        u'type': module.params.get('type'),
        u'httpHealthCheck': HealthCheckHttphealthcheck(module.params.get('http_health_check', {}), module).to_request(),
        u'httpsHealthCheck': HealthCheckHttpshealthcheck(module.params.get('https_health_check', {}), module).to_request(),
        u'tcpHealthCheck': HealthCheckTcphealthcheck(module.params.get('tcp_health_check', {}), module).to_request(),
        u'sslHealthCheck': HealthCheckSslhealthcheck(module.params.get('ssl_health_check', {}), module).to_request()
    }
    return_vals = {}
    for k, v in request.items():
        if v is not None:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/healthChecks/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/healthChecks".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
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
        u'checkIntervalSec': response.get(u'checkIntervalSec'),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'healthyThreshold': response.get(u'healthyThreshold'),
        u'id': response.get(u'id'),
        u'name': module.params.get('name'),
        u'timeoutSec': response.get(u'timeoutSec'),
        u'unhealthyThreshold': response.get(u'unhealthyThreshold'),
        u'type': response.get(u'type'),
        u'httpHealthCheck': HealthCheckHttphealthcheck(response.get(u'httpHealthCheck', {}), module).from_response(),
        u'httpsHealthCheck': HealthCheckHttpshealthcheck(response.get(u'httpsHealthCheck', {}), module).from_response(),
        u'tcpHealthCheck': HealthCheckTcphealthcheck(response.get(u'tcpHealthCheck', {}), module).from_response(),
        u'sslHealthCheck': HealthCheckSslhealthcheck(response.get(u'sslHealthCheck', {}), module).from_response()
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/global/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#healthCheck')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], 'message')
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation')
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class HealthCheckHttphealthcheck(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({
            u'host': self.request.get('host'),
            u'requestPath': self.request.get('request_path'),
            u'response': self.request.get('response'),
            u'port': self.request.get('port'),
            u'portName': self.request.get('port_name'),
            u'proxyHeader': self.request.get('proxy_header')
        })

    def from_response(self):
        return remove_nones_from_dict({
            u'host': self.request.get(u'host'),
            u'requestPath': self.request.get(u'requestPath'),
            u'response': self.request.get(u'response'),
            u'port': self.request.get(u'port'),
            u'portName': self.request.get(u'portName'),
            u'proxyHeader': self.request.get(u'proxyHeader')
        })


class HealthCheckHttpshealthcheck(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({
            u'host': self.request.get('host'),
            u'requestPath': self.request.get('request_path'),
            u'response': self.request.get('response'),
            u'port': self.request.get('port'),
            u'portName': self.request.get('port_name'),
            u'proxyHeader': self.request.get('proxy_header')
        })

    def from_response(self):
        return remove_nones_from_dict({
            u'host': self.request.get(u'host'),
            u'requestPath': self.request.get(u'requestPath'),
            u'response': self.request.get(u'response'),
            u'port': self.request.get(u'port'),
            u'portName': self.request.get(u'portName'),
            u'proxyHeader': self.request.get(u'proxyHeader')
        })


class HealthCheckTcphealthcheck(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({
            u'request': self.request.get('request'),
            u'response': self.request.get('response'),
            u'port': self.request.get('port'),
            u'portName': self.request.get('port_name'),
            u'proxyHeader': self.request.get('proxy_header')
        })

    def from_response(self):
        return remove_nones_from_dict({
            u'request': self.request.get(u'request'),
            u'response': self.request.get(u'response'),
            u'port': self.request.get(u'port'),
            u'portName': self.request.get(u'portName'),
            u'proxyHeader': self.request.get(u'proxyHeader')
        })


class HealthCheckSslhealthcheck(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({
            u'request': self.request.get('request'),
            u'response': self.request.get('response'),
            u'port': self.request.get('port'),
            u'portName': self.request.get('port_name'),
            u'proxyHeader': self.request.get('proxy_header')
        })

    def from_response(self):
        return remove_nones_from_dict({
            u'request': self.request.get(u'request'),
            u'response': self.request.get(u'response'),
            u'port': self.request.get(u'port'),
            u'portName': self.request.get(u'portName'),
            u'proxyHeader': self.request.get(u'proxyHeader')
        })


if __name__ == '__main__':
    main()
