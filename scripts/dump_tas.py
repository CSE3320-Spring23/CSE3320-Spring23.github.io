#!/usr/bin/env python3

import yaml

for index, ta in enumerate(yaml.safe_load(open('static/yaml/tas.yaml')), 1):
    #print(f'{index}. {ta["name"]} {ta["netid"]}@mavs.uta.edu {ta["github"]}')
    print(f'{ta["netid"]}')
