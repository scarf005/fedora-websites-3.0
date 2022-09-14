#!/bin/bash
# Recover po from already translated yaml files

for file in $(find content/ -type f | grep -v en.yml); do 
  yaml2po -t $(dirname $file)/index.en.yml -i $file -o $(sed 's/content/locales/;s/.yml/.po/' <<<$file);
done
