#!/bin/bash

# Make sure we exit(1) if there is an error
set -e
echo "test" > test.html
aws s3 cp test.html s3://registry.opendata.aws/test.html
aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DIST_ID --paths "/*"
exit 1
