#!/bin/bash

# Make sure we exit(1) if there is an error
set -e


# Check file extension, should be .yaml
echo "Validating filenames..."
if ls datasets | grep -vE '^[a-z 0-9\_\-]+\.yaml$'
then
    echo "are invalid; please ensure names end in '.yaml' and contain only lowercase letters, numbers, hyphens, or underscores."
    exit 1
else
    echo "all valid!"
fi


# Validate yaml
echo "Validating yamls against schema..."
ls datasets |
    xargs -P20 -I{} bash -c "pykwalify -q -d datasets/{} -s schema.yaml && exit 0 || echo {} failed validation; exit 1"
