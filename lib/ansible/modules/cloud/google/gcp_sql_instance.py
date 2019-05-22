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
module: gcp_sql_instance
description:
- Represents a Cloud SQL instance. Cloud SQL instances are SQL databases hosted in
  Google's cloud. The Instances resource provides methods for common configuration
  and management tasks.
short_description: Creates a GCP Instance
version_added: 2.7
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
  backend_type:
    description:
    - "* FIRST_GEN: First Generation instance. MySQL only."
    - "* SECOND_GEN: Second Generation instance or PostgreSQL instance."
    - "* EXTERNAL: A database server that is not managed by Google."
    - 'Some valid choices include: FIRST_GEN, SECOND_GEN, EXTERNAL'
    required: false
  connection_name:
    description:
    - Connection name of the Cloud SQL instance used in connection strings.
    required: false
  database_version:
    description:
    - The database engine type and version. For First Generation instances, can be
      MYSQL_5_5, or MYSQL_5_6. For Second Generation instances, can be MYSQL_5_6 or
      MYSQL_5_7. Defaults to MYSQL_5_6.
    - 'PostgreSQL instances: POSTGRES_9_6 The databaseVersion property can not be
      changed after instance creation.'
    - 'Some valid choices include: MYSQL_5_5, MYSQL_5_6, MYSQL_5_7, POSTGRES_9_6'
    required: false
  failover_replica:
    description:
    - The name and status of the failover replica. This property is applicable only
      to Second Generation instances.
    required: false
    suboptions:
      name:
        description:
        - The name of the failover replica. If specified at instance creation, a failover
          replica is created for the instance. The name doesn't include the project
          ID. This property is applicable only to Second Generation instances.
        required: false
  instance_type:
    description:
    - The instance type. This can be one of the following.
    - "* CLOUD_SQL_INSTANCE: A Cloud SQL instance that is not replicating from a master."
    - "* ON_PREMISES_INSTANCE: An instance running on the customer's premises."
    - "* READ_REPLICA_INSTANCE: A Cloud SQL instance configured as a read-replica."
    - 'Some valid choices include: CLOUD_SQL_INSTANCE, ON_PREMISES_INSTANCE, READ_REPLICA_INSTANCE'
    required: false
  ipv6_address:
    description:
    - The IPv6 address assigned to the instance. This property is applicable only
      to First Generation instances.
    required: false
  master_instance_name:
    description:
    - The name of the instance which will act as master in the replication setup.
    required: false
  max_disk_size:
    description:
    - The maximum disk size of the instance in bytes.
    required: false
  name:
    description:
    - Name of the Cloud SQL instance. This does not include the project ID.
    required: true
  region:
    description:
    - The geographical region. Defaults to us-central or us-central1 depending on
      the instance type (First Generation or Second Generation/PostgreSQL).
    required: false
  replica_configuration:
    description:
    - Configuration specific to failover replicas and read replicas.
    required: false
    suboptions:
      failover_target:
        description:
        - Specifies if the replica is the failover target. If the field is set to
          true the replica will be designated as a failover replica.
        - In case the master instance fails, the replica instance will be promoted
          as the new master instance.
        - Only one replica can be specified as failover target, and the replica has
          to be in different zone with the master instance.
        required: false
        type: bool
      mysql_replica_configuration:
        description:
        - MySQL specific configuration when replicating from a MySQL on-premises master.
          Replication configuration information such as the username, password, certificates,
          and keys are not stored in the instance metadata. The configuration information
          is used only to set up the replication connection and is stored by MySQL
          in a file named master.info in the data directory.
        required: false
        suboptions:
          ca_certificate:
            description:
            - PEM representation of the trusted CA's x509 certificate.
            required: false
          client_certificate:
            description:
            - PEM representation of the slave's x509 certificate .
            required: false
          client_key:
            description:
            - PEM representation of the slave's private key. The corresponding public
              key is encoded in the client's certificate.
            required: false
          connect_retry_interval:
            description:
            - Seconds to wait between connect retries. MySQL's default is 60 seconds.
            required: false
          dump_file_path:
            description:
            - Path to a SQL dump file in Google Cloud Storage from which the slave
              instance is to be created. The URI is in the form gs://bucketName/fileName.
              Compressed gzip files (.gz) are also supported. Dumps should have the
              binlog co-ordinates from which replication should begin. This can be
              accomplished by setting --master-data to 1 when using mysqldump.
            required: false
          master_heartbeat_period:
            description:
            - Interval in milliseconds between replication heartbeats.
            required: false
          password:
            description:
            - The password for the replication connection.
            required: false
          ssl_cipher:
            description:
            - A list of permissible ciphers to use for SSL encryption.
            required: false
          username:
            description:
            - The username for the replication connection.
            required: false
          verify_server_certificate:
            description:
            - Whether or not to check the master's Common Name value in the certificate
              that it sends during the SSL handshake.
            required: false
            type: bool
      replica_names:
        description:
        - The replicas of the instance.
        required: false
      service_account_email_address:
        description:
        - The service account email address assigned to the instance. This property
          is applicable only to Second Generation instances.
        required: false
  settings:
    description:
    - The user settings.
    required: false
    suboptions:
      ip_configuration:
        description:
        - The settings for IP Management. This allows to enable or disable the instance
          IP and manage which external networks can connect to the instance. The IPv4
          address cannot be disabled for Second Generation instances.
        required: false
        suboptions:
          ipv4_enabled:
            description:
            - Whether the instance should be assigned an IP address or not.
            required: false
            type: bool
          authorized_networks:
            description:
            - The list of external networks that are allowed to connect to the instance
              using the IP. In CIDR notation, also known as 'slash' notation (e.g.
              192.168.100.0/24).
            required: false
            suboptions:
              expiration_time:
                description:
                - The time when this access control entry expires in RFC 3339 format,
                  for example 2012-11-15T16:19:00.094Z.
                required: false
              name:
                description:
                - An optional label to identify this entry.
                required: false
              value:
                description:
                - The whitelisted value for the access control list. For example,
                  to grant access to a client from an external IP (IPv4 or IPv6) address
                  or subnet, use that address or subnet here.
                required: false
          require_ssl:
            description:
            - Whether the mysqld should default to 'REQUIRE X509' for users connecting
              over IP.
            required: false
            type: bool
      tier:
        description:
        - The tier or machine type for this instance, for example db-n1-standard-1.
          For MySQL instances, this field determines whether the instance is Second
          Generation (recommended) or First Generation.
        required: false
      availability_type:
        description:
        - The availabilityType define if your postgres instance is run zonal or regional.
        - 'Some valid choices include: ZONAL, REGIONAL'
        required: false
      backup_configuration:
        description:
        - The daily backup configuration for the instance.
        required: false
        suboptions:
          enabled:
            description:
            - Enable Autobackup for your instance.
            required: false
            type: bool
          binary_log_enabled:
            description:
            - Whether binary log is enabled. If backup configuration is disabled,
              binary log must be disabled as well. MySQL only.
            required: false
            type: bool
          start_time:
            description:
            - Define the backup start time in UTC (HH:MM) .
            required: false
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: create a instance
  gcp_sql_instance:
    name: "{{resource_name}}-2"
    settings:
      ip_configuration:
        authorized_networks:
        - name: google dns server
          value: 8.8.8.8/32
      tier: db-n1-standard-1
    region: us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
backendType:
  description:
  - "* FIRST_GEN: First Generation instance. MySQL only."
  - "* SECOND_GEN: Second Generation instance or PostgreSQL instance."
  - "* EXTERNAL: A database server that is not managed by Google."
  returned: success
  type: str
connectionName:
  description:
  - Connection name of the Cloud SQL instance used in connection strings.
  returned: success
  type: str
databaseVersion:
  description:
  - The database engine type and version. For First Generation instances, can be MYSQL_5_5,
    or MYSQL_5_6. For Second Generation instances, can be MYSQL_5_6 or MYSQL_5_7.
    Defaults to MYSQL_5_6.
  - 'PostgreSQL instances: POSTGRES_9_6 The databaseVersion property can not be changed
    after instance creation.'
  returned: success
  type: str
failoverReplica:
  description:
  - The name and status of the failover replica. This property is applicable only
    to Second Generation instances.
  returned: success
  type: complex
  contains:
    available:
      description:
      - The availability status of the failover replica. A false status indicates
        that the failover replica is out of sync. The master can only failover to
        the failover replica when the status is true.
      returned: success
      type: bool
    name:
      description:
      - The name of the failover replica. If specified at instance creation, a failover
        replica is created for the instance. The name doesn't include the project
        ID. This property is applicable only to Second Generation instances.
      returned: success
      type: str
instanceType:
  description:
  - The instance type. This can be one of the following.
  - "* CLOUD_SQL_INSTANCE: A Cloud SQL instance that is not replicating from a master."
  - "* ON_PREMISES_INSTANCE: An instance running on the customer's premises."
  - "* READ_REPLICA_INSTANCE: A Cloud SQL instance configured as a read-replica."
  returned: success
  type: str
ipAddresses:
  description:
  - The assigned IP addresses for the instance.
  returned: success
  type: complex
  contains:
    ipAddress:
      description:
      - The IP address assigned.
      returned: success
      type: str
    timeToRetire:
      description:
      - The due time for this IP to be retired in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.
        This field is only available when the IP is scheduled to be retired.
      returned: success
      type: str
    type:
      description:
      - The type of this IP address. A PRIMARY address is an address that can accept
        incoming connections. An OUTGOING address is the source address of connections
        originating from the instance, if supported.
      returned: success
      type: str
ipv6Address:
  description:
  - The IPv6 address assigned to the instance. This property is applicable only to
    First Generation instances.
  returned: success
  type: str
masterInstanceName:
  description:
  - The name of the instance which will act as master in the replication setup.
  returned: success
  type: str
maxDiskSize:
  description:
  - The maximum disk size of the instance in bytes.
  returned: success
  type: int
name:
  description:
  - Name of the Cloud SQL instance. This does not include the project ID.
  returned: success
  type: str
region:
  description:
  - The geographical region. Defaults to us-central or us-central1 depending on the
    instance type (First Generation or Second Generation/PostgreSQL).
  returned: success
  type: str
replicaConfiguration:
  description:
  - Configuration specific to failover replicas and read replicas.
  returned: success
  type: complex
  contains:
    failoverTarget:
      description:
      - Specifies if the replica is the failover target. If the field is set to true
        the replica will be designated as a failover replica.
      - In case the master instance fails, the replica instance will be promoted as
        the new master instance.
      - Only one replica can be specified as failover target, and the replica has
        to be in different zone with the master instance.
      returned: success
      type: bool
    mysqlReplicaConfiguration:
      description:
      - MySQL specific configuration when replicating from a MySQL on-premises master.
        Replication configuration information such as the username, password, certificates,
        and keys are not stored in the instance metadata. The configuration information
        is used only to set up the replication connection and is stored by MySQL in
        a file named master.info in the data directory.
      returned: success
      type: complex
      contains:
        caCertificate:
          description:
          - PEM representation of the trusted CA's x509 certificate.
          returned: success
          type: str
        clientCertificate:
          description:
          - PEM representation of the slave's x509 certificate .
          returned: success
          type: str
        clientKey:
          description:
          - PEM representation of the slave's private key. The corresponding public
            key is encoded in the client's certificate.
          returned: success
          type: str
        connectRetryInterval:
          description:
          - Seconds to wait between connect retries. MySQL's default is 60 seconds.
          returned: success
          type: int
        dumpFilePath:
          description:
          - Path to a SQL dump file in Google Cloud Storage from which the slave instance
            is to be created. The URI is in the form gs://bucketName/fileName. Compressed
            gzip files (.gz) are also supported. Dumps should have the binlog co-ordinates
            from which replication should begin. This can be accomplished by setting
            --master-data to 1 when using mysqldump.
          returned: success
          type: str
        masterHeartbeatPeriod:
          description:
          - Interval in milliseconds between replication heartbeats.
          returned: success
          type: int
        password:
          description:
          - The password for the replication connection.
          returned: success
          type: str
        sslCipher:
          description:
          - A list of permissible ciphers to use for SSL encryption.
          returned: success
          type: str
        username:
          description:
          - The username for the replication connection.
          returned: success
          type: str
        verifyServerCertificate:
          description:
          - Whether or not to check the master's Common Name value in the certificate
            that it sends during the SSL handshake.
          returned: success
          type: bool
    replicaNames:
      description:
      - The replicas of the instance.
      returned: success
      type: list
    serviceAccountEmailAddress:
      description:
      - The service account email address assigned to the instance. This property
        is applicable only to Second Generation instances.
      returned: success
      type: str
settings:
  description:
  - The user settings.
  returned: success
  type: complex
  contains:
    ipConfiguration:
      description:
      - The settings for IP Management. This allows to enable or disable the instance
        IP and manage which external networks can connect to the instance. The IPv4
        address cannot be disabled for Second Generation instances.
      returned: success
      type: complex
      contains:
        ipv4Enabled:
          description:
          - Whether the instance should be assigned an IP address or not.
          returned: success
          type: bool
        authorizedNetworks:
          description:
          - The list of external networks that are allowed to connect to the instance
            using the IP. In CIDR notation, also known as 'slash' notation (e.g. 192.168.100.0/24).
          returned: success
          type: complex
          contains:
            expirationTime:
              description:
              - The time when this access control entry expires in RFC 3339 format,
                for example 2012-11-15T16:19:00.094Z.
              returned: success
              type: str
            name:
              description:
              - An optional label to identify this entry.
              returned: success
              type: str
            value:
              description:
              - The whitelisted value for the access control list. For example, to
                grant access to a client from an external IP (IPv4 or IPv6) address
                or subnet, use that address or subnet here.
              returned: success
              type: str
        requireSsl:
          description:
          - Whether the mysqld should default to 'REQUIRE X509' for users connecting
            over IP.
          returned: success
          type: bool
    tier:
      description:
      - The tier or machine type for this instance, for example db-n1-standard-1.
        For MySQL instances, this field determines whether the instance is Second
        Generation (recommended) or First Generation.
      returned: success
      type: str
    availabilityType:
      description:
      - The availabilityType define if your postgres instance is run zonal or regional.
      returned: success
      type: str
    backupConfiguration:
      description:
      - The daily backup configuration for the instance.
      returned: success
      type: complex
      contains:
        enabled:
          description:
          - Enable Autobackup for your instance.
          returned: success
          type: bool
        binaryLogEnabled:
          description:
          - Whether binary log is enabled. If backup configuration is disabled, binary
            log must be disabled as well. MySQL only.
          returned: success
          type: bool
        startTime:
          description:
          - Define the backup start time in UTC (HH:MM) .
          returned: success
          type: str
    settingsVersion:
      description:
      - The version of instance settings. This is a required field for update method
        to make sure concurrent updates are handled properly. During update, use the
        most recent settingsVersion value for this instance and do not try to update
        this value.
      returned: success
      type: int
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
            backend_type=dict(type='str'),
            connection_name=dict(type='str'),
            database_version=dict(type='str'),
            failover_replica=dict(type='dict', options=dict(name=dict(type='str'))),
            instance_type=dict(type='str'),
            ipv6_address=dict(type='str'),
            master_instance_name=dict(type='str'),
            max_disk_size=dict(type='int'),
            name=dict(required=True, type='str'),
            region=dict(type='str'),
            replica_configuration=dict(
                type='dict',
                options=dict(
                    failover_target=dict(type='bool'),
                    mysql_replica_configuration=dict(
                        type='dict',
                        options=dict(
                            ca_certificate=dict(type='str'),
                            client_certificate=dict(type='str'),
                            client_key=dict(type='str'),
                            connect_retry_interval=dict(type='int'),
                            dump_file_path=dict(type='str'),
                            master_heartbeat_period=dict(type='int'),
                            password=dict(type='str'),
                            ssl_cipher=dict(type='str'),
                            username=dict(type='str'),
                            verify_server_certificate=dict(type='bool'),
                        ),
                    ),
                    replica_names=dict(type='list', elements='str'),
                    service_account_email_address=dict(type='str'),
                ),
            ),
            settings=dict(
                type='dict',
                options=dict(
                    ip_configuration=dict(
                        type='dict',
                        options=dict(
                            ipv4_enabled=dict(type='bool'),
                            authorized_networks=dict(
                                type='list', elements='dict', options=dict(expiration_time=dict(type='str'), name=dict(type='str'), value=dict(type='str'))
                            ),
                            require_ssl=dict(type='bool'),
                        ),
                    ),
                    tier=dict(type='str'),
                    availability_type=dict(type='str'),
                    backup_configuration=dict(
                        type='dict', options=dict(enabled=dict(type='bool'), binary_log_enabled=dict(type='bool'), start_time=dict(type='str'))
                    ),
                ),
            ),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/sqlservice.admin']

    state = module.params['state']
    kind = 'sql#instance'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind, fetch)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind, fetch)
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
    auth = GcpSession(module, 'sql')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind, fetch):
    auth = GcpSession(module, 'sql')
    return wait_for_operation(module, auth.put(link, resource_to_request(module)))


def delete(module, link, kind, fetch):
    auth = GcpSession(module, 'sql')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'sql#instance',
        u'backendType': module.params.get('backend_type'),
        u'connectionName': module.params.get('connection_name'),
        u'databaseVersion': module.params.get('database_version'),
        u'failoverReplica': InstanceFailoverreplica(module.params.get('failover_replica', {}), module).to_request(),
        u'instanceType': module.params.get('instance_type'),
        u'ipv6Address': module.params.get('ipv6_address'),
        u'masterInstanceName': module.params.get('master_instance_name'),
        u'maxDiskSize': module.params.get('max_disk_size'),
        u'name': module.params.get('name'),
        u'region': module.params.get('region'),
        u'replicaConfiguration': InstanceReplicaconfiguration(module.params.get('replica_configuration', {}), module).to_request(),
        u'settings': InstanceSettings(module.params.get('settings', {}), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'sql')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/sql/v1beta4/projects/{project}/instances/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/sql/v1beta4/projects/{project}/instances".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    # SQL only: return on 403 if not exist
    if allow_not_found and response.status_code == 403:
        return None

    try:
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
        u'backendType': response.get(u'backendType'),
        u'connectionName': response.get(u'connectionName'),
        u'databaseVersion': response.get(u'databaseVersion'),
        u'failoverReplica': InstanceFailoverreplica(response.get(u'failoverReplica', {}), module).from_response(),
        u'instanceType': response.get(u'instanceType'),
        u'ipAddresses': InstanceIpaddressesArray(response.get(u'ipAddresses', []), module).from_response(),
        u'ipv6Address': response.get(u'ipv6Address'),
        u'masterInstanceName': response.get(u'masterInstanceName'),
        u'maxDiskSize': response.get(u'maxDiskSize'),
        u'name': response.get(u'name'),
        u'region': response.get(u'region'),
        u'replicaConfiguration': InstanceReplicaconfiguration(response.get(u'replicaConfiguration', {}), module).from_response(),
        u'settings': InstanceSettings(response.get(u'settings', {}), module).from_response(),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/sql/v1beta4/projects/{project}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'sql#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'sql#instance')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'sql#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class InstanceFailoverreplica(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'name': self.request.get('name')})

    def from_response(self):
        return remove_nones_from_dict({u'name': self.request.get(u'name')})


class InstanceIpaddressesArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'ipAddress': item.get('ip_address'), u'timeToRetire': item.get('time_to_retire'), u'type': item.get('type')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'ipAddress': item.get(u'ipAddress'), u'timeToRetire': item.get(u'timeToRetire'), u'type': item.get(u'type')})


class InstanceReplicaconfiguration(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'failoverTarget': self.request.get('failover_target'),
                u'mysqlReplicaConfiguration': InstanceMysqlreplicaconfiguration(self.request.get('mysql_replica_configuration', {}), self.module).to_request(),
                u'replicaNames': self.request.get('replica_names'),
                u'serviceAccountEmailAddress': self.request.get('service_account_email_address'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'failoverTarget': self.request.get(u'failoverTarget'),
                u'mysqlReplicaConfiguration': InstanceMysqlreplicaconfiguration(
                    self.request.get(u'mysqlReplicaConfiguration', {}), self.module
                ).from_response(),
                u'replicaNames': self.request.get(u'replicaNames'),
                u'serviceAccountEmailAddress': self.request.get(u'serviceAccountEmailAddress'),
            }
        )


class InstanceMysqlreplicaconfiguration(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'caCertificate': self.request.get('ca_certificate'),
                u'clientCertificate': self.request.get('client_certificate'),
                u'clientKey': self.request.get('client_key'),
                u'connectRetryInterval': self.request.get('connect_retry_interval'),
                u'dumpFilePath': self.request.get('dump_file_path'),
                u'masterHeartbeatPeriod': self.request.get('master_heartbeat_period'),
                u'password': self.request.get('password'),
                u'sslCipher': self.request.get('ssl_cipher'),
                u'username': self.request.get('username'),
                u'verifyServerCertificate': self.request.get('verify_server_certificate'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'caCertificate': self.request.get(u'caCertificate'),
                u'clientCertificate': self.request.get(u'clientCertificate'),
                u'clientKey': self.request.get(u'clientKey'),
                u'connectRetryInterval': self.request.get(u'connectRetryInterval'),
                u'dumpFilePath': self.request.get(u'dumpFilePath'),
                u'masterHeartbeatPeriod': self.request.get(u'masterHeartbeatPeriod'),
                u'password': self.request.get(u'password'),
                u'sslCipher': self.request.get(u'sslCipher'),
                u'username': self.request.get(u'username'),
                u'verifyServerCertificate': self.request.get(u'verifyServerCertificate'),
            }
        )


class InstanceSettings(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'ipConfiguration': InstanceIpconfiguration(self.request.get('ip_configuration', {}), self.module).to_request(),
                u'tier': self.request.get('tier'),
                u'availabilityType': self.request.get('availability_type'),
                u'backupConfiguration': InstanceBackupconfiguration(self.request.get('backup_configuration', {}), self.module).to_request(),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'ipConfiguration': InstanceIpconfiguration(self.request.get(u'ipConfiguration', {}), self.module).from_response(),
                u'tier': self.request.get(u'tier'),
                u'availabilityType': self.request.get(u'availabilityType'),
                u'backupConfiguration': InstanceBackupconfiguration(self.request.get(u'backupConfiguration', {}), self.module).from_response(),
            }
        )


class InstanceIpconfiguration(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'ipv4Enabled': self.request.get('ipv4_enabled'),
                u'authorizedNetworks': InstanceAuthorizednetworksArray(self.request.get('authorized_networks', []), self.module).to_request(),
                u'requireSsl': self.request.get('require_ssl'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'ipv4Enabled': self.request.get(u'ipv4Enabled'),
                u'authorizedNetworks': InstanceAuthorizednetworksArray(self.request.get(u'authorizedNetworks', []), self.module).from_response(),
                u'requireSsl': self.request.get(u'requireSsl'),
            }
        )


class InstanceAuthorizednetworksArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'expirationTime': item.get('expiration_time'), u'name': item.get('name'), u'value': item.get('value')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'expirationTime': item.get(u'expirationTime'), u'name': item.get(u'name'), u'value': item.get(u'value')})


class InstanceBackupconfiguration(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {u'enabled': self.request.get('enabled'), u'binaryLogEnabled': self.request.get('binary_log_enabled'), u'startTime': self.request.get('start_time')}
        )

    def from_response(self):
        return remove_nones_from_dict(
            {u'enabled': self.request.get(u'enabled'), u'binaryLogEnabled': self.request.get(u'binaryLogEnabled'), u'startTime': self.request.get(u'startTime')}
        )


if __name__ == '__main__':
    main()
