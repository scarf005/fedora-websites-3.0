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
    results['ga'] = {'x86_64': {}, 'aarch64': {}}
    results['beta'] = {'x86_64': {}, 'aarch64': {}}

    # 1 - transform release vars into an image name we want to query for
    # "Fedora-Cloud-Base-AmazonEC2.x86_64-41-Prerelease-1.2
    templates = [
        (f"Fedora-Cloud-Base-AmazonEC2.x86_64-{release['ga']['releasever']}-{release['ga']['rc_version']}", {
            'x86_64_base_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') in ('gp2', 'gp3'),
        }),
        (f"Fedora-Cloud-Base-AmazonEC2.aarch64-{release['ga']['releasever']}-{release['ga']['rc_version']}", {
            'aarch64_base_AMI': lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') in ('gp2', 'gp3'),
        }),
        (f"Fedora-Cloud-Base-AmazonEC2.x86_64-{release['beta']['releasever']}-Prerelease-{release['beta']['rc_version']}", {
            'pre_X86_64_base_AMI':  lambda e: e.get('virt_type') == 'hvm' and e.get('vol_type') in ('gp2', 'gp3'),
        }),
        (f"Fedora-Cloud-Base-AmazonEC2.aarch64-{release['beta']['releasever']}-Prerelease-{release['beta']['rc_version']}", {
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
                print(upload)
                arch = upload['architecture']
                stage = "beta" if "pre_" in name else "ga"
                for region, ami in upload['regions'].items():
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


"""
{
  "body": {
    "architecture": "x86_64",
    "compose_id": "Fedora-41-20240911.0",
    "image_name": "Fedora-Cloud-Base-AmazonEC2.x86_64-41-Prerelease-1.2",
    "regions": {
      "af-south-1": "ami-0cc8a1f67b7c1c5f1",
      "ap-east-1": "ami-0035534588bcf26c6",
      "ap-northeast-1": "ami-0a8f87ddd0dd81b86",
      "ap-northeast-2": "ami-0271d3396e8fd47b2",
      "ap-northeast-3": "ami-0ddb62e440d7421c2",
      "ap-south-1": "ami-014f3a3d500eec583",
      "ap-southeast-1": "ami-0565ceee1fae87071",
      "ap-southeast-2": "ami-02a4cef299e6f62e9",
      "ap-southeast-3": "ami-006cf910b9f0d4f35",
      "ca-central-1": "ami-03815b87e17c5af65",
      "eu-central-1": "ami-07f57d366d384c4d8",
      "eu-north-1": "ami-0cc16a6386a73523a",
      "eu-south-1": "ami-0d968c2edb1d2d904",
      "eu-west-1": "ami-096b0e83fe32a74bb",
      "eu-west-2": "ami-0e8bd6f40f6eaeeaf",
      "eu-west-3": "ami-02fcced94b7006d03",
      "me-south-1": "ami-0f1289dd9aa44638a",
      "sa-east-1": "ami-07a5a678b00ccc48a",
      "us-east-1": "ami-0a1a3731a749a16db",
      "us-east-2": "ami-078663b68885f0ae5",
      "us-west-1": "ami-0ea86d67aba82be5a",
      "us-west-2": "ami-01ef26235a840d0d6"
    }
  },
  "headers": {
    "fedora_messaging_schema": "fedora_image_uploader.published.v1.aws",
    "fedora_messaging_severity": 20,
    "priority": 0,
    "sent-at": "2024-09-12T01:55:05+00:00"
  },
  "id": "16856f57-56f9-4335-ba34-6c62a3b4f13b",
  "priority": 0,
  "queue": null,
  "topic": "org.fedoraproject.prod.fedora_image_uploader.published.v1.aws.Cloud_Base.41.x86_64"
}
"""