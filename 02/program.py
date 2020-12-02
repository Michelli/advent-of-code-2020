import os
import re
import sys


def read_input(filename):
    # Open input file as list
    with open(os.path.join(sys.path[0], filename)) as input:
        entries = input.read().splitlines()
    # Close input.txt
        input.close()
    # Return list
    return entries


def part_one():
    entries = read_input("input.txt")

    # Total valid passwords
    valid_count = 0

    for line in entries:
        # Create named groups
        regex = re.match(r"(?P<min>^\d+)-(?P<max>\d+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+$)", line)
        
        # Variables
        min_times = int(regex.group('min'))
        max_times = int(regex.group('max'))
        counter = 0

        # Check password
        for letter in regex.group('password'):
            if letter == regex.group('letter'):
                counter += 1

        # Increase counter if password is valid
        if counter >= min_times and counter <= max_times:
            valid_count += 1

    return valid_count