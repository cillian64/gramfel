#!/usr/bin/env python3

import sys
import random
import subprocess

if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = "sayings.txt"

f = open(path)
sayings = f.readlines()
saying = random.choice(sayings).strip()

subprocess.call(["say", "-vRalph", saying])
