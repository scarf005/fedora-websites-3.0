#!/bin/bash
# Generate yaml file from po when translation is above $THRESHOLD % completion
THRESHOLD=0

for file in $(find locales/ -type f -name \*.po); do
  yaml_dir=$(dirname ${file/locales/content})
  pagename=$(basename ${yaml_dir})
  yaml_filename=$(basename ${file/.po/.yml})
  template=$(dirname ${yaml_dir})/$pagename.yml
  output=$(dirname ${yaml_dir})/${yaml_filename}

  if [ -f $template ]; then
    echo compiling ${file} to ${output}..
    po2yaml -t ${template} -i ${file} -o ${output} --threshold=$THRESHOLD;
  fi
done

