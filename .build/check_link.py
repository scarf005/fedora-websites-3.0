#!/usr/bin/python
# vim:syntax=python:ts=2:sts=2:sw=2:set expandtab:

import yaml
import json
import requests
import os
import sys

from argparse import ArgumentParser

class colors:
  FAIL = '\033[91m'
  OK = '\033[92m'
  END = '\033[0m'

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


def parse_args(args):
    usage = """
          check_link.py [-b|--beta]
          Check download links from compose metadata
          """
    parser = ArgumentParser(usage=usage)
    parser.add_argument("-b", "--beta",action="store_true", dest="beta", help="Check beta artifacts")
    opts = parser.parse_args(args)
    return opts


def merge_overrides(md, ovr):
  for key, value in ovr.items():
    if key in md and isinstance(md[key], dict) and isinstance(value, dict):
      merge_overrides(md[key], value)
    else:
      md[key] = value


def load_release(beta):
  global FVERS
  global FRC
  global META_URL
  global BETA
  global OVERRIDES
  with open("../content/release.yml", 'r') as f:
    rel = yaml.safe_load(f)
  if beta:
    key = 'beta'
    BETA = "test/"
  else: 
    key = 'ga'
    BETA = ""
  FRC = rel[key]['rc_version']
  FVERS = rel[key]['releasever']
  OVERRIDES = rel[key]['compose_overrides'] if 'compose_overrides' in rel[key] else None
  META_URL = f"https://kojipkgs.fedoraproject.org/compose/{FVERS}/latest-Fedora-{FVERS}/compose/metadata/images.json"


def check_download_link(link):
    r = requests.head(link, allow_redirects=True)
    if r.status_code != 200:
        print(f'[{colors.FAIL}KO: {r.status_code}{colors.END}] {link}')
        return False
    print(f'[{colors.OK}OK{colors.END}] {link}')
    return True


if __name__ == '__main__':
  opts = parse_args(sys.argv[1:])
  load_release(opts.beta)
  r = requests.get(META_URL)
  if r.status_code != 200:
    raise Exception(f"Metadata not found at {META_URL}!")
  j = r.json()
  artifacts = j['payload']['images']
  if OVERRIDES:
    merge_overrides(artifacts, OVERRIDES)
  cksums = []
  rc = []
  print()
  print("Checking download artifacts...")
  for k,v in j['payload']['images'].items():
    print()
    print(f"{k}:")
    for arch,v in v.items():
      for art in v:
        basepath = f"{dlpath[art['arch']]}/{FVERS}" if not opts.beta else f"{dlpath[art['arch']]}/test/{FVERS}_Beta"
        if k == "Spins":
          basepath = f"{spinpath[art['arch']]}/{FVERS}" if not opts.beta else f"{spinpath[art['arch']]}/test//{FVERS}_Beta"
        if k == "Labs":
          basepath = f"{labspath[art['arch']]}/{FVERS}" if not opts.beta else f"{labspath[art['arch']]}/test/{FVERS}_Beta"
        link = f"{basepath}/{art['path']}"
        if 'dl_prefix' in art:
          link = f"{art['dl_prefix'].replace('/download.','/dl.')}/{art['path']}"
        rc.append(check_download_link(link))
        subpath = os.path.dirname(art['path'])
        art_format = 'iso' if art['format'] == 'iso' else 'images'
        if 'checksum_file' in art:
          cksum = f"{basepath}/{art['checksum_file']}"
          if 'dl_prefix' in art:
            cksum = f"{art['dl_prefix'].replace('/download.','/dl.')}/{art['checksum_file']}"
        else:
          cksum = f"{basepath}/{subpath}/Fedora-{k}-{FVERS}-{FRC}-{arch}-CHECKSUM" if not opts.beta else f"{basepath}/{subpath}/Fedora-{k}-{art_format}-{FVERS}_Beta-{FRC}-{arch}-CHECKSUM"
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
  
