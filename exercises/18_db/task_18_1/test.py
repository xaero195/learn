import yaml


with open('switches.yml') as f:
    templates = yaml.safe_load(f)

print(templates)
