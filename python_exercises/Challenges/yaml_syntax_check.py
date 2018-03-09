import yaml

with open("vars.yml", 'r') as stream:
    try:
        print (yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)