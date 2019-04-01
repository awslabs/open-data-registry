#!/bin/bash

# Make sure we exit(1) if there is an error
set -e

# For our use case, we can ignore loading warnings
PYTHONWARNINGS=ignore::yaml.YAMLLoadWarning

for f in datasets/*
do
  echo $f
  pykwalify -d $f -s schema.yaml -q
done
