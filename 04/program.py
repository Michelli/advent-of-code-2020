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


def part_two(filename):
    passports = create_entries(filename)
    valid_passports = 0

    for passport in passports:
        # Repeat checks of part one
        value_names = re.findall(r"[a-z]{3}(?=:)", passport)

        # Start second test
        if len(value_names) == 8 or len(value_names) == 7 and 'cid' not in value_names:
            # Passport rules passed
            check_counter = 0

            # Birth year: Between 1920-2002
            if len(re.findall(r"(?<=byr:)19[2-9]\d|200[0-2]", passport)) > 0:
                check_counter += 1

            # Eye colour: List of colour codes
            if len(re.findall(r"(?<=ecl:(amb|blu|brn|gry|grn|hzl|oth))", passport)) > 0:
                check_counter += 1

            # Expiration year: Between 2020-2030
            if len(re.findall(r"(?<=eyr:)20(?:(?:2\d)|(?:30))", passport)) > 0:
                check_counter += 1

            # Hair colour: Colour hex code with leading hashtag
            if len(re.findall(r"(?<=hcl:)#[0-9a-f]{6}", passport)) > 0:
                check_counter += 1

            # Height: Between 150-193cm OR 59-76in
            if len(re.findall(r"(?<=hgt:)1(?:[5-8]\d|9[0-3])cm|(?:59|6\d|7[0-6])in", passport)) > 0:
                check_counter += 1

            # Issue year: Between 2010-2020
            if len(re.findall(r"(?<=iyr:)20(?:(?:1\d)|(?:20))", passport)) > 0:
                check_counter += 1

            # Passport ID: Nine digits
            if len(re.findall(r"(?<=pid:)\d{9}(?=\s|\n|$)", passport)) > 0:
                check_counter += 1

            # All checks passed
            if check_counter == 7:
                valid_passports += 1

    return valid_passports
