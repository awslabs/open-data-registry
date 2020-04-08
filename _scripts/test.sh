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

  # Apply schema
  pykwalify -d $f -s schema.yaml -q
done