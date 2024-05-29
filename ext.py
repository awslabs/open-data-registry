import re
import yaml
import requests
import time
from urllib3.exceptions import InsecureRequestWarning

# Suppress the warning on Verify=False requests
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

tags = yaml.safe_load(open("tags.yaml"))
tags.append("aws-pds")

adx_categories = yaml.safe_load(open("adx_categories.yaml"))

resources = yaml.safe_load(open("resources.yaml"))
services = yaml.safe_load(open("services.yaml"))

arn_regex = re.compile(r"^arn:(aws|aws-iso):.+:.*:.*:.+$")
host_regex = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,63})(\/.*)*\/?$")
controlled_access_regex = re.compile(
    r"^(https?:\/\/)?([\da-z\.\-\_]+)\.([a-z\.]{2,63})(\/.*)*\/?$"
)
explore_regex = re.compile(r"^\[.+\]\(https?:\/\/[\w\d.\-\/#\?\&\%=]+\)$")


def retry(howmany):
    def tryFunc(func):
        def f(*args, **kwargs):
            attempts = 0
            while attempts < howmany:
                try:
                    return func(*args, **kwargs)
                except:
                    attempts += 1
                    time.sleep(1.0 * 4.0 ** attempts)
                    if attempts >= howmany:
                        raise

        return f

    return tryFunc


# Check if provided tags are in tags.yaml
def ext_tags(value, rule_obj, path):
    if value not in tags:
        print("Invalid tag!", value)
        return False

    # If we're here, all tags were ok
    return True

# Check if provided ADX categories are in adx_categories.yaml
def ext_adx_categories(value, rule_obj, path):
    if value not in adx_categories:
        print("Invalid ADX category!", value)
        return False

    # If we're here, all categories were ok
    return True    


# Check if provided resources are in resources.yaml
def ext_resources(value, rule_obj, path):
    if value not in resources:
        print("Invalid resource!", value)
        return False

    # If we're here, all resources were ok
    return True


# Check if provided services are in services.yaml
def ext_services(value, rule_obj, path):
    if value not in services:
        print("Invalid service!", value)
        return False

    # If we're here, all services were ok
    return True


# Check to make sure we have a valid arn
def ext_resources_arn(value, rule_obj, path):

    if not re.fullmatch(arn_regex, value):
        print(
            "ARN '{}' is not valid, it should like like arn:aws:s3:::yourbucket".format(
                value
            )
        )
        return False

    return True


# Check to make sure we have a valid host
def ext_resources_host(value, rule_obj, path):

    if not re.fullmatch(host_regex, value):
        print("Host '{}' is not valid".format(value))
        return False

    return True


# Check to make sure we have a valid controlled access string
def ext_resources_controlled_access(value, rule_obj, path):

    if not re.fullmatch(controlled_access_regex, value):
        print("Controlled Access string '{}' is not valid".format(value))
        return False

    return True


# Check to make sure we have a valid array of links
def ext_resources_explore(value, rule_obj, path):

    if not re.fullmatch(explore_regex, value):
        print("Explore string '{}' is not a valid link".format(value))
        return False

    return True
