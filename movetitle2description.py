#!/bin/python

# Move title value to description
import yaml
import argparse

parser = argparse.ArgumentParser(
    description='Generate software verification cases from a requirements yml file')
parser.add_argument('requirements',
                    help='Name of requirements file')

args = parser.parse_args()

with open(args.requirements, 'r') as file:
    parsed_reqs = yaml.safe_load(file)

requirements = parsed_reqs.get('requirements')

# print(parsed_reqs)
# print("------------")
# print(requirements)

reqs = []
index = 1
for req in requirements:
    tmpReq = {}
    for key in req:
        if key == 'title':
            tmpReq['title'] = " "
            tmpReq['description'] = req[key]
        elif key == 'description':
            pass
        else:
            tmpReq[key] = req[key]
    reqs.append(tmpReq)

reqs_content = {}

for key in parsed_reqs:
    if key == 'requirements':
        reqs_content[key] = reqs
    else:
        reqs_content[key] = parsed_reqs[key]

with open('req_' + args.requirements, 'w') as file:
    yaml.dump(reqs_content, file, indent=2, sort_keys=False)
