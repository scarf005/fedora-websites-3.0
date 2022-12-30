#!/bin/env python

import yaml
import json
import re

url_re = re.compile(r'^(?:http|ftp)s?://')

with open('../content/events/flock.yml', 'r') as f:
  nuxt_content = yaml.safe_load(f)

try:
  with open('flock.json', 'r') as f:
    old_locale = json.load(f)
except FileNotFoundError:
  old_locale = {}
new_locale = {}

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
      elif isinstance(v, str) and is_valid(v):
        add_key(v)

def is_valid(s):
  if not len(s):
    return False
  if s.startswith('public/'):
    return False
  if re.match(url_re, s):
    return False
  return True


def add_key(k):
  if k not in new_locale:
    if k not in old_locale:
      safe = k.replace('{', "{'{'}").replace('}', "{'}'}").replace('$', "{'$'}").replace('|', "{'|'}").replace('@', "{'@'}")
    else:
      safe = old_locale[k]
    new_locale[k] = safe

parse_dict(nuxt_content)

with open('flock.json', 'w') as f:
  json.dump(new_locale, f, indent=2, sort_keys=True)
