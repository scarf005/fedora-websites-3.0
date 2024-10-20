#!/usr/bin/python
# vim:syntax=python:ts=2:sts=2:sw=2:set expandtab:

import yaml
import json
import requests


dlpath = {
  "x86_64": "https://download.fedoraproject.org/pub/fedora/linux/releases",
  "aarch64": "https://download.fedoraproject.org/pub/fedora/linux/releases",
  "s390x": "https://download.fedoraproject.org/pub/fedora-secondary/releases",
  "ppc64le": "https://download.fedoraproject.org/pub/fedora-secondary/releases",
}
labspath = {
  "x86_64": "https://download.fedoraproject.org/pub/alt/releases",
  "aarch64": "https://download.fedoraproject.org/pub/fedora/linux/releases",
}
spinpath = {
  "x86_64": "https://download.fedoraproject.org/pub/fedora/linux/releases",
  "aarch64": "https://download.fedoraproject.org/pub/fedora/linux/releases",
}
iotpath = "https://download.fedoraproject.org/pub/alt/iot"


def merge_overrides(md, ovr):
  for key, value in ovr.items():
    if key in md and isinstance(md[key], dict) and isinstance(value, dict):
      merge_overrides(md[key], value)
    else:
      md[key] = value


def fmw_release(version, beta=False, overrides={}):
  META_URL = f"https://kojipkgs.fedoraproject.org/compose/{version}/latest-Fedora-{version}/compose/metadata/images.json"
  version_path = f"test/{version}" if beta else version
  IOT_META_URL = f"https://dl.fedoraproject.org/pub/alt/iot/{version_path}/metadata/images.json"
  
  r = requests.get(META_URL)
  if r.status_code != 200:
    raise Exception(f"Metadata not found at {META_URL}!")
  j = r.json()
  artifacts = j['payload']['images']

  r = requests.get(IOT_META_URL)
  if r.status_code == 200:
    iot = r.json()
    artifacts["IoT"] = iot['payload']['images']["IoT"]

  if overrides:
    merge_overrides(artifacts, overrides)

  fmw_release = []
  for k,v in artifacts.items():
    for arch,v in v.items():
      for art in v:
        basepath = f"{dlpath[art['arch']]}/{version}" if not beta else f"{dlpath[art['arch']]}/test/{version}_Beta"
        if k == "Spins":
          basepath = f"{spinpath[art['arch']]}/{version}" if not beta else f"{spinpath[art['arch']]}/test/{version}_Beta"
        if k == "Labs":
          basepath = f"{labspath[art['arch']]}/{version}" if not beta else f"{labspath[art['arch']]}/test/{version}_Beta"
        if k == "IoT":
          basepath = f"{iotpath}/{version}" if not beta else f"{iotpath}/test/{version}"
        link = f"{basepath}/{art['path']}"
        if 'dl_prefix' in art:
          link = f"{art['dl_prefix']}/{art['path']}"

        fmw_release.append({
          "version": f"{version} Beta" if beta else f"{version}",
          "arch": art["arch"],
          "link": link,
          "variant": k,
          "subvariant": art["subvariant"],
          "sha256": f"{art["checksums"]["sha256"]}",
          "size": f"{art["size"]}"
        })

  return fmw_release

if __name__ == '__main__':
  with open("../content/release.yml", 'r') as f:
    rel = yaml.safe_load(f)
  fmw_releases = []
  # beta
  if rel["beta"]["enabled"]:
    fmw_releases.extend(fmw_release(rel["beta"]["releasever"], beta = True))
  # GA
  fmw_releases.extend(fmw_release(rel["ga"]["releasever"], overrides=rel["ga"]["compose_overrides"]))
  fmw_releases.extend(fmw_release(rel["ga"]["releasever"]-1))

  print(json.dumps(fmw_releases, indent=2))
