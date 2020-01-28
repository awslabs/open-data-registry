#!/bin/bash

echo Current branch is $CODEBUILD_WEBHOOK_HEAD_REF and source is $CODEBUILD_SOURCE_VERSION

if [[ "$CODEBUILD_WEBHOOK_HEAD_REF" == "refs/heads/master" && ${CODEBUILD_SOURCE_VERSION:0:3} != "pr/" ]]; then
    echo Deploying to S3 and invalidating CloudFront cache.

	# Sync files to S3, removing files that no longer exist
	aws s3 sync open-data-registry-browser/dist/ s3://registry.opendata.aws/ --delete

	# Invalidate CDN cache
	aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DIST_ID --paths "/*"
else
    echo No deploy needed.
fi
