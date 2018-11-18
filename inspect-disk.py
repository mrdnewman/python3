#!/usr/bin/env python3

#
# obtain-remote-data-with-ansible-s-api/
#

import sys
import json
import ansible.runner

# specify hosts from inventory we should contact
hostlist = [ 'sparse01', 'sparse02', 'sparse03' ]

def gigs(kibs):
    return float(kibs) / 1024.0 / 1024.0

runner = ansible.runner.Runner(
    module_name='my-df',
    module_args='',
    remote_user='root',
    sudo=False,
    pattern=':'.join(hostlist),
)

# Ansible now pops off to do it's thing via SSH
response = runner.run()

# We're back.
# Check for failed hosts

if 'dark' in response:
    if len(response['dark']) > 0:
        print("Contact failures:")
        for host, reason in response['dark'].iteritems():
            print("  %s (%s)" % (host, reason['msg']))

total = 0.0
for host, res in response['contacted'].iteritems():
    print(host)
    for fs in res['space']:
        gb = gigs(fs['available'])
        total += gb
        print("  %-30s %10.2f" % (fs['mountpoint'], gb))

print("Total space over %d hosts: %.2f GB" % (len(response['contacted']), total))
