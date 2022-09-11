#!/bin/bash
# Compile yaml file from po when translation is above $THRESHOLD % completion
THRESHOLD=0

for file in $(find locales/ -type f -name \*.po); do
  echo compiling ${file}..
  po2yaml -t $(dirname ${file/locales/content})/index.en.yml -i $file -o $(sed 's/locales/content/;s/.po/.yml/' <<<$file) --threshold=$THRESHOLD;
done

