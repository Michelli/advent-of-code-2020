import os
import re
import sys


def create_entries(filename):
    # Open input file as list
    with open(os.path.join(sys.path[0], filename)) as input:
        entries = input.read().split("\n\n")
    # Close input.txt
    input.close()
    # Return list
    return entries


def part_one(filename):
    passports = create_entries(filename)
    counter = 0

    for passport in passports:
        # Check values
        value_names = re.findall(r"[a-z]{3}(?=:)", passport)

        # Valid if all 8 fields are present
        # Or if only cid field is missing
        if len(value_names) == 8 or len(value_names) == 7 and 'cid' not in value_names:
            counter += 1

    return counter
