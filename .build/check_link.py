#!/usr/bin/python
# vim:syntax=python:ts=2:sts=2:sw=2:set expandtab:

import yaml
import json
import requests
import os
import sys


dlpath = {
  "x86_64": "https://dl.fedoraproject.org/pub/fedora/linux/releases",
  "aarch64": "https://dl.fedoraproject.org/pub/fedora/linux/releases",
  "s390x": "https://dl.fedoraproject.org/pub/fedora-secondary/releases",
  "ppc64le": "https://dl.fedoraproject.org/pub/fedora-secondary/releases",
}
labspath = {
  "x86_64": "https://dl.fedoraproject.org/pub/alt/releases",
  "aarch64": "https://dl.fedoraproject.org/pub/fedora-secondary/releases",
}
spinpath = {
  "x86_64": "https://dl.fedoraproject.org/pub/fedora/linux/releases",
  "aarch64": "https://dl.fedoraproject.org/pub/fedora-secondary/releases",
}


def load_release():
  global FVERS
  global FRC
  global META_URL
  with open("../content/release.yml", 'r') as f:
    rel = yaml.safe_load(f)
  FVERS = rel['ga']['releasever']
  FRC = rel['ga']['rc_version']
  META_URL = f"https://kojipkgs.fedoraproject.org/compose/{FVERS}/latest-Fedora-{FVERS}/compose/metadata/images.json"


def check_download_link(link):
    r = requests.head(link, allow_redirects=True)
    if r.status_code != 200:
        print('[BROKEN LINK] %s' % link)
        return False
    print('[OK] %s' % link)
    return True


if __name__ == '__main__':
  load_release()
  r = requests.get(META_URL)
  if r.status_code != 200:
    raise Exception(f"Metadata not found at {META_URL}!")
  j = r.json()
  cksums = []
  rc = []
  print()
  print("Checking download artifacts...")
  for k,v in j['payload']['images'].items():
    print()
    print(f"{k}:")
    for arch,v in v.items():
      for art in v:
        basepath = f"{dlpath[art['arch']]}/{FVERS}"
        if k == "Spins":
          basepath = f"{spinpath[art['arch']]}/{FVERS}"
        if k == "Labs":
          basepath = f"{labspath[art['arch']]}/{FVERS}"
        link = f"{basepath}/{art['path']}"
        rc.append(check_download_link(link))
        subpath = os.path.dirname(art['path'])
        cksum = f"{basepath}/{subpath}/Fedora-{k}-{FVERS}-{FRC}-{arch}-CHECKSUM"
        if cksum not in cksums:
          cksums.append(cksum)
  
  print()
  print("Checking CHECKSUM...")
  for cksum in cksums:
    rc.append(check_download_link(cksum))


  print()
  print("***********************")
  if False in rc:
    print("SOME LINKS ARE BROKEN!")
    sys.exit(1)
  else:
    print("All Good!")
    sys.exit(0)
  
