import yaml


# Check if provided tags are in tags.yaml
def ext_tags(value, rule_obj, path):
    tags = yaml.load(open('tags.yaml'))
    tags.append('aws-pds')
    if value not in tags:
        print('Invalid tag!', value)
        return False

    # If we're here, all tags were ok
    return True


# Check if provided resources are in resources.yaml
def ext_resources(value, rule_obj, path):
    resources = yaml.load(open('resources.yaml'))
    if value not in resources:
        print('Invalid resource!', value)
        return False

    # If we're here, all resources were ok
    return True
