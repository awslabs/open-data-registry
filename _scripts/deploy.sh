#!/bin/bash

echo Current branch is $CODEBUILD_WEBHOOK_HEAD_REF

if [[ "$CODEBUILD_WEBHOOK_HEAD_REF" == "refs/heads/master" ]]; then
    echo Deploying to S3 and invalidating CloudFront cache.

	# Sync files to S3, removing files that no longer exist
	aws s3 sync open-data-registry-browser/dist/ s3://test-roda/ --delete

	# Invalidate CDN cache
	aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DIST_ID --paths "/*"
else
    echo No deploy needed.
fi
