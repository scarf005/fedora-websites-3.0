#!/bin/bash
# Generate POT files from yaml

for file in $(find content -type f -name \*.en.yml); do 
  mkdir -p $(dirname ${file/content/locales})
  yaml2po -P -i $file -o $(sed 's/content/locales/;s/.yml/.pot/' <<<$file);
done
