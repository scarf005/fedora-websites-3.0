#!/bin/bash
# Generate CMS Config

cat ./schema/* > ./config.yml

# for item in ./schema; do
#   if [ -d "$item" ];
#   then
#     cat "$item"/* >> configTest.yml
#   else
#     cat "$item" >> configTest.yml
#   fi
# done