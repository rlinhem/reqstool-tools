#!/bin/python

import yaml
import argparse

parser = argparse.ArgumentParser(
    description="Generate software verification cases from a requirements yml file"
)
parser.add_argument("requirements", help="Name of requirements file")

args = parser.parse_args()

with open(args.requirements, "r") as file:
    parsed_reqs = yaml.safe_load(file)

requirements = parsed_reqs.get("requirements")

svcs = []
index = 1
for req in requirements:
    svc = {}
    svc["id"] = "svc" + str(index).zfill(3)
    svc["requirement_ids"] = [req["id"]]
    svc["title"] = req["title"]
    svc["description"] = req["description"]
    svc["verification"] = (
        req["verification"] if "verification" in req else "automated (test)"
    )
    svc["instructions"] = "TBD"
    svc["revision"] = "0.0.1"
    svcs.append(svc)
    index = index + 1

svc_content = {}
svc_content["version"] = "0.0.1"
svc_content["cases"] = svcs

with open("svc_" + args.requirements, "w") as file:
    yaml.dump(svc_content, file, indent=2, sort_keys=False)
