#!/usr/bin/python
""" Return the AMIs uploaded by fedimg for a given set of release vars.

Search datagrepper to find the results.

Deps:  $ sudo dnf install python-requests

Author:     Ralph Bean <rbean@redhat.com>
License:    LGPLv2+
"""

from __future__ import print_function

import collections
import functools
from datetime import datetime, timedelta
from hashlib import sha1
import logging
import shelve
import os
import sys
from argparse import ArgumentParser
import yaml

import pprint
from fedimg_vars_lib import get_messages, sanity_check, mocked_fedimg, check_permissions

logging.basicConfig(level=logging.INFO)

log = logging.getLogger('fetch_amis')

cachefile = '/tmp/fedoraproject_cloud_ami_%s.cache'


# We cache this guy on disk for 500s
def collect(release):
    filename = cachefile % (sha1(str(release).encode()).hexdigest())
    shelf = shelve.open(filename)
    # check_permissions(filename=filename)
    if shelf.get('timestamp') and shelf.get('timestamp') > (datetime.utcnow() - timedelta(hours=1)):
        log.info('Retrieving release data from shelf')
        toreturn = shelf['collected']
        shelf.close()
        return toreturn

    results = {}
    results['ga'] = {'x86_64': {}, 'arm64': {}}
    results['beta'] = {'x86_64': {}, 'arm64': {}}

    # 1 - transform release vars into an image name we want to query for
    templates = [
        (f"Fedora-Cloud-Base-{release['ga']['releasever']}-{release['ga']['rc_version']}.x86_64", {
            'x86_64_base_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') in ('gp2', 'gp3'),
        }),
        (f"Fedora-Cloud-Base-{release['ga']['releasever']}-{release['ga']['rc_version']}.aarch64", {
            'aarch64_base_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') in ('gp2', 'gp3'),
        }),
        (f"Fedora-Cloud-Base-{release['beta']['releasever']}_Beta-{release['beta']['rc_version']}.x86_64", {
            'pre_X86_64_base_AMI':  lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') in ('gp2', 'gp3'),
        }),
        (f"Fedora-Cloud-Base-{release['beta']['releasever']}_Beta-{release['beta']['rc_version']}.aarch64", {
            'pre_AARCH64_base_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') in ('gp2', 'gp3'),
        }),
    ]


    for target, buckets in templates:
        # 2 - Build an intermediary dict
        intermediary = collections.OrderedDict()
        log.info("Looking for AMIs for %s" % target)

        messages = get_messages(target)
        for message in messages:
            key = message['msg']['image_name']
            if not key in intermediary:
                intermediary[key] = []
            intermediary[key].append(message['msg'])

        if not intermediary:
            log.warn("No AMIs found for %s" % target)
            continue

        # What would this even mean?
        assert len(intermediary) < 2, "Impossible.  Got more than one target."

        uploads = intermediary[target]

        # 3- transform intermediary representation into results
        for name, matches in buckets.items():
            for upload in uploads:
                if matches(upload['extra']):
                    ami = upload['extra']['id']
                    region = upload['destination']
                    arch = upload['architecture']
                    stage = "beta" if "pre_" in name else "ga"
                    results[stage][arch][region] = ami

    shelf['timestamp'] = datetime.utcnow()
    shelf['collected'] = results
    shelf.close()

    return results

def parse_args(args):
    usage = """
          fetch_amis.py input output
          Retrieve AMIs list from datagrepper using release info from <input> and save it to <output>
          """
    parser = ArgumentParser(usage=usage)
    parser.add_argument("input", help="input YAML file with release information")
    parser.add_argument("output", help="output YAML file")
    opts = parser.parse_args(args)
    return opts

if __name__ == "__main__":
  opts = parse_args(sys.argv[1:])

  with open(opts.input, 'r') as f:
    y = yaml.safe_load(f)
  

  logging.info(y)
  data = collect(y)
  logging.info(yaml.dump(data))
  with open(opts.output, 'w') as f:
    f.write(yaml.dump(data))
