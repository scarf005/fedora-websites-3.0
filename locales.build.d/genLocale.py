#!/bin/env python3

import yaml
import json
import re
import sys
import os

from argparse import ArgumentParser

url_re = re.compile(r'^(?:http|ftp)s?://')


def parse_args(args):
    usage = """
          genLocale.py file.yaml
          Extract strings from CMS yaml file and save them in json
          """
    parser = ArgumentParser(usage=usage)
    parser.add_argument("yamlfile", help="the YAML file used to extract strings")
    parser.add_argument("--all", dest="all", action="store_true", help="scan all yaml files")
    parser.add_argument("-o", dest="output", help="output JSON file")
    opts = parser.parse_args(args)
    return opts


def parse_list(l):
  if isinstance(l, list):
    for i in l:
      if isinstance(i, dict):
        parse_dict(i)
      elif isinstance(i, list):
        parse_list(i)
      elif isinstance(i, str) and len(i):
        add_key(i)


def parse_dict(d):
  if isinstance(d, dict):
    for k, v in d.items():
      if isinstance(v, dict):
        parse_dict(v)
      elif isinstance(v, list):
        parse_list(v)
      elif isinstance(v, str) and is_valid(v) and not any(pattern.match(k) for pattern in ignore_keys):
        add_key(v)


def is_valid(s):
  if not len(s):
    return False
  if s.startswith('public/'):
    return False
  if any(pattern.fullmatch(s) for pattern in ignore_values):
    return False
  if re.match(url_re, s):
    return False
  return True


def add_key(k):
  if k not in new_locale:
    new_locale[k] = k.replace('$', "{'$'}").replace('|', "{'|'}").replace('@', "{'@'}")


def gen_outname(infile):
  if infile.startswith('./') or infile.startswith('../') or infile.startswith('/'):
    outname = '_'.join(infile.split('/')[2::]).replace('.yml','.json')
  else:
    outname = '_'.join(infile.split('/')[1::]).replace('.yml','.json')
  return outname

def extract_str(yamlfile, output=None):
  with open(yamlfile, 'r') as f:
    nuxt_content = yaml.safe_load(f)
    
  parse_dict(nuxt_content)
  
  if output:
    with open(output, 'w') as f:
      json.dump(new_locale, f, indent=2, sort_keys=True)
  else:
      print(json.dumps(new_locale, indent=2, sort_keys=True))


if __name__ == "__main__":
  opts = parse_args(sys.argv[1:])
  s_path = os.path.dirname(sys.argv[0])

  with open(os.path.join(s_path, "genLocale.cfg.yml")) as f:
    config = yaml.safe_load(f)
  ignore_files = list(map(re.compile, config['ignore_files']))
  ignore_keys = list(map(re.compile, config['ignore_keys']))
  ignore_values = list(map(re.compile, config['ignore_values']))

  if opts.all:
    for root,dirs,files in os.walk(opts.yamlfile):
      for file in filter(lambda f: f.endswith('.yml'), files):
        content_file = os.path.join(root, file)
        output_file = gen_outname(content_file)
        if any(pattern.fullmatch(output_file) for pattern in ignore_files):
          continue
        print(f"{content_file} -> {output_file}")

        new_locale = {} # yes, I know....
        extract_str(content_file, os.path.join(s_path, "cms_content", output_file))
  else:
    new_locale = {}
    extract_str(opts.yamlfile, opts.output)
