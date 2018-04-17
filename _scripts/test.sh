#!/bin/bash

# Make sure we exit(1) if there is an error
set -e

for f in datasets/*
do
  echo $f
  pykwalify -d $f -s schema.yaml
done