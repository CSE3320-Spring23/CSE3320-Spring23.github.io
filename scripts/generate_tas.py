#!/usr/bin/env python3

import csv
import random
import glob
import sys
import yaml

TAS      = [ta['github'] for ta in yaml.safe_load(open('static/yaml/tas.yaml'))]
STUDENTS = []

for student in open('static/csv/students.csv', 'r'):
    STUDENTS.append(student.strip())

CONFLICTS = dict(
    (ta['github'], ta['conflicts'])
    for ta in yaml.safe_load(open('static/yaml/tas.yaml'))
    if ta.get('conflicts')
)

HAS_CONFLICTS = True


while HAS_CONFLICTS:
    random.shuffle(STUDENTS)
    random.shuffle(TAS)

    TAS           = TAS * (len(STUDENTS) // len(TAS) + 1)
    MAPPING       = list(sorted(map(list, zip(STUDENTS, TAS))))
    HAS_CONFLICTS = False

    for ta, conflicts in CONFLICTS.items():
        for conflict in conflicts:
            if [conflict, ta] in MAPPING:
                HAS_CONFLICTS = True

print(yaml.dump(MAPPING, default_flow_style=False))
