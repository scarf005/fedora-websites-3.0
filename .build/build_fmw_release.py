#!/usr/bin/env python
import fedfind.release
import json
import sys
import yaml
from argparse import ArgumentParser

IOT_URL = "https://download.fedoraproject.org/pub/alt/iot"
IOT_BETA_URL = "https://download.fedoraproject.org/pub/alt/iot/test"


def hashify(version, milestone, arch, link, variant, subvariant):
    return {
        "version": version,
        "arch": arch,
        "link": link,
        "variant": variant,
        "subvariant": subvariant,
    }


def list_releases(releases):
    out = []
    final_vers = int(releases["ga"]["releasever"])

    iot = fedfind.release.get_release(url="/".join((IOT_URL, str(final_vers))))
    iot._version = str(final_vers)
    iot.__class__ = fedfind.release.Pungi4Mirror

    out.append(fedfind.release.get_release(final_vers, milestone="final"))
    out.append(iot)

    if releases["beta"]["enabled"]:
        beta_vers = int(releases["beta"]["releasever"])
        out.append(fedfind.release.get_release(beta_vers, milestone="beta"))
        iot_beta = fedfind.release.get_release(
            url="/".join((IOT_BETA_URL, str(beta_vers)))
        )
        iot_beta._version = f"{beta_vers} beta"
        iot_beta.__class__ = fedfind.release.Pungi4Mirror
        out.append(iot_beta)

    return out


def parse_args(args):
    usage = """
          build_fmw_release.py input output
          """
    parser = ArgumentParser(usage=usage)
    parser.add_argument("input", help="input YAML file with release information")
    parser.add_argument("output", help="output JSON file")
    opts = parser.parse_args(args)
    return opts


if __name__ == "__main__":
    opts = parse_args(sys.argv[1:])

    with open(opts.input, "r") as f:
        y = yaml.safe_load(f)

    output = []
    for rel in list_releases(y):
        for img in rel.all_images:
            location = img["url"]
            h = hashify(
                rel.version,
                rel.milestone,
                img["arch"],
                location,
                img["variant"],
                img["subvariant"],
            )

            if "checksums" in img and "sha256" in img["checksums"]:
                h["sha256"] = str(img["checksums"]["sha256"])

            if "size" in img:
                h["size"] = str(img["size"])

            output.append(h)

    with open(opts.output, "w") as f:
        json.dump(output, f, indent=2)
