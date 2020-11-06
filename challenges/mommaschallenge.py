#!/usr/bin/python3

# mommas.json challenge

import json

file= open("mommas.json", "r").read()

mommas= json.loads(file)

print(mommas)
