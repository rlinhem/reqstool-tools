#!/bin/python

import yaml
import argparse
from functools import reduce

parser = argparse.ArgumentParser(
    description="Compare requirements and svc, list requirements missing svc"
)
parser.add_argument("-r", "--requirements_file", help="Name of requirements file")
parser.add_argument(
    "-svc",
    "--software_verification_file",
    help="Name of software_verification_cases file",
)

args = parser.parse_args()

with open(args.requirements_file, "r") as file:
    parsed_reqs = yaml.safe_load(file)

with open(args.software_verification_file, "r") as file:
    parsed_svcs = yaml.safe_load(file)

requirements = parsed_reqs.get("requirements")
svcs = parsed_svcs.get("cases")

# Collected all requerement ids that is referenced in svcs

referd_reqs = [reqid for svc in svcs for reqid in svc["requirement_ids"]]

refed_reqs = [reqid.removeprefix("ext-topsky-swim-icd:") for reqid in referd_reqs]
## map(lambda reqid: reqid.removeprefix("ext-topsky-swim-icd:"), referd_reqs)
reqs_missing_svc = [req["id"] for req in requirements if req["id"] not in refed_reqs]


print("------------------")
print(*reqs_missing_svc, sep="\n")
