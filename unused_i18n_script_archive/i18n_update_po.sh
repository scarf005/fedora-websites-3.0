#!/bin/bash
# Update PO files with the latest version of the POT

for file in $(find locales/ -type f -name \*.po); do
  pot_dir=$(dirname ${file})
  pagename=$(basename ${pot_dir})
  pot_file=${pot_dir}/${pagename}.pot

  if [ -f $pot_file ]; then
    echo updating ${file}..
    pot2po --nofuzzymatching -i ${pot_file} -t ${file} -o ${file};
  fi
done

