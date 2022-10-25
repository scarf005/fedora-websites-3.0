#!/bin/bash
# Generate POT files from yaml

for file in $(find content -type f -name \*.yml); do 
  pagename=$(basename $file .yml)
  output_dir=$(dirname ${file/content/locales})/${pagename}
  output=${output_dir}/${pagename}.pot
  mkdir -p ${output_dir}
  yaml2po -P -i $file -o $output;

  # Flag url & image keys as read-only
  sed -i "/^#.*\([uU][rR][lLiI]\|[iI]mage\)$/i #, read-only" $output
done
