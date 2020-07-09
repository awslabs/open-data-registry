import yaml
import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress the warning on Verify=False requests
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

tags = yaml.safe_load(open('tags.yaml'))
tags.append('aws-pds')

resources = yaml.safe_load(open('resources.yaml'))
services = yaml.safe_load(open('services.yaml'))

# Check if provided tags are in tags.yaml
def ext_tags(value, rule_obj, path):
    if value not in tags:
        print('Invalid tag!', value)
        return False

    # If we're here, all tags were ok
    return True


# Check if provided resources are in resources.yaml
def ext_resources(value, rule_obj, path):
    if value not in resources:
        print('Invalid resource!', value)
        return False

    # If we're here, all resources were ok
    return True

# Check if provided services are in services.yaml
def ext_services(value, rule_obj, path):
    if value not in services:
        print('Invalid service!', value)
        return False

    # If we're here, all services were ok
    return True

def ext_valid_bucket_regions(value, rule_obj, path):

    # Make sure this is a dict, and a bucket, then validate the region
    if isinstance(value, dict) and 'Type' in value and value['Type'] == 'S3 Bucket':
        bucket = value['ARN']
        parts = bucket.split(':::')
        if not parts[0] == 'arn:aws:s3':
            # This is probably not on public aws so we can't check
            return True
        bucket = parts[1]
        parts = bucket.split('/')
        bucket = parts[0]
        url = "https://{}.s3.amazonaws.com".format(bucket)

        # Get the headers for this bucket.
        # Verify=False because the wildcard matching doesn't work for buckets with '.'
        r = requests.head(url, verify=False)

        if r.status_code == requests.codes.not_found:
            print("Bucket {} doesn't exist or there was a momentary glitch".format(bucket))
            return False

        if not 'x-amz-bucket-region' in r.headers:
            print("Bucket region missing from request header?")
            return False

        region = r.headers['x-amz-bucket-region']
        if not value['Region'].lower() == region.lower():
            print('The region for bucket {} is listed as {} but is actually {}'.format(bucket, value['Region'], region))
            return False


    return True
