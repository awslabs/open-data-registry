#!/bin/bash

# Sync files to S3, removing files that no longer exist
aws s3 sync open-data-registry-browser/dist/ s3://test-roda/ --delete

# Invalidate CDN cache
aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DIST_ID --paths "/*"
