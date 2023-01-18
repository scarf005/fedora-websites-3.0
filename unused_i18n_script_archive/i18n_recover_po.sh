#!/bin/bash
# Recreate PO files from the old one before CMS structural changes
# Once migrated, old po file is deleted
# THIS SHOULD ONLY BE USED ONCE AS PART OF THE STRUCTURAL CHANGE
# pot2po --nofuzzymatching -i locales/editions/workstation/home.pot -t locales/pages/editions/workstation/home/index.fr.po locales/editions/workstation/home.fr.po

for file in $(find locales/pages -type f -name \*.po); do
  pot_dir=$(dirname ${file/pages\//})
  pagename=$(basename ${pot_dir})
  source_po_name=$(basename ${file})
  pot_file=${pot_dir}/${pagename}.pot
  po_file=${pot_dir}/${source_po_name/index/$pagename}

  if [ -f $pot_file ]; then
    echo creating ${po_file}...
    pot2po --nofuzzymatching -i $pot_file -t $file -o $po_file;
    rm -v $file
  fi
done

