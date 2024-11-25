#!/bin/python

import yaml
import argparse

parser = argparse.ArgumentParser(description="Generate list of review svc")
parser.add_argument("svc", help="Name of svc file")

args = parser.parse_args()

print("arg ", args.svc)
with open(args.svc, "r") as file:
    parsed_reqs = yaml.safe_load(file)

svcs = parsed_reqs.get("cases")

# print(parsed_reqs)
## print("------------")
# print(svcs)

# revs = filter(lambda svc: svc["verification"] == "review", svcs)
# ids = map(lambda svc: svc["id"], revs)
## print(list(ids))
# print(*ids, sep="\n")
print("------------------")
des_revs = filter(lambda svc: "Review of design" in svc["instructions"], svcs)
des_ids = map(lambda svc: svc["id"], des_revs)
print(*des_ids, sep="\n")
# with open("review_svcs", "w") as file:
#    yaml.dump(revs, file, indent=2, sort_keys=False)
