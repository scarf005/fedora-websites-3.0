#!/bin/bash
# Generate POT files from yaml

for file in $(find content -type f -name \*.en.yml); do 
  mkdir -p $(dirname ${file/content/locales})
  output=$(sed 's/content/locales/;s/.yml/.pot/' <<<$file)
  yaml2po -P -i $file -o $output;

  # Flag url & image keys as read-only
  sed -i "/^#.*\([uU]rl\|[iI]mage\)$/i #, read-only" $output
done
