#!/usr/bin/env bash

set -eux

export ANSIBLE_ROLES_PATH=../

# Test graceful failure for older versions of botocore
ansible-playbook -i ../../inventory -e @../../integration_config.yml -v playbooks/full_test.yml "$@"
