#!/bin/bash

# Make sure we exit(1) if there is an error
set -e

for f in datasets/*
do
  echo $f

  # Check file extension, should be .yaml
  if [ ${f: -5} != ".yaml" ]
  then
    continue
  fi

  added=`git log --format="%ai" --reverse $f | head -1 | cut -d " " -f 1`
  modified=`git log --format="%ai" $f | head -1 | cut -d " " -f 1`

  printf "\nRegistryEntryAdded: \"$added\"\n" >>$f
  printf "RegistryEntryLastModified: \"$modified\"\n" >>$f

done
