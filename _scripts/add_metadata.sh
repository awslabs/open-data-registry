#!/bin/bash

# Make sure we exit(1) if there is an error
set -e
echo "this might be a security issue" > test.html
aws s3 sync test.html s3://registry.opendata.aws/test.html
aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DIST_ID --paths "/*"
exit 1
