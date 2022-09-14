#!/bin/bash
# Update PO files with the latest version of the POT

for file in $(find locales/ -type f -name \*.po); do
  echo updating ${file}..
  pot2po -i $(dirname ${file})/index.en.pot -t $file -o $file;
done

