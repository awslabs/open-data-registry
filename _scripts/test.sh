#!/bin/bash

# Make sure we exit(1) if there is an error
set -e

for f in datasets/*
do
  echo $f

  # Check file extension, should be .yaml
  if [ ${f: -5} != ".yaml" ]
  then
    echo Error: Exiting because file extension shoud be .yaml
    exit 1
  fi

  # Check file name is all lower case
  if [ ${f} != ${f,,} ]
  then
        echo Error: Exiting because file name should be all lower case
        exit 1
  fi

  # Apply schema
  pykwalify -d $f -s schema.yaml -q
done
