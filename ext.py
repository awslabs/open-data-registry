import yaml


# Check if provided tags are in tags.yaml
def ext_tags(value, rule_obj, path):
    tags = yaml.load(open('tags.yaml'))
    if value not in tags:
        print('Invalid tag!', value)
        return False

    # If we're here, all tags were ok
    return True
