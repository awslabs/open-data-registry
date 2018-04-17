#!/bin/bash

# Copy files to S3
aws s3 cp open-data-registry-browser/dist/ s3://registry.opendata.aws/ --recursive

# Invalidate CDN cache
aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DIST_ID --paths "/*"