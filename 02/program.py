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


def part_one(filename):
    entries = read_input(filename)

    # Total valid passwords
    valid_count = 0

    for line in entries:
        # Create named groups
        regex = re.match(
            r"(?P<min>^\d+)-(?P<max>\d+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+$)", line)

        # Variables
        counter = 0
        min_times = int(regex.group('min'))
        max_times = int(regex.group('max'))

        # Check password
        for letter in regex.group('password'):
            if letter == regex.group('letter'):
                counter += 1

        # Increase counter if password is valid
        if counter >= min_times and counter <= max_times:
            valid_count += 1

    return valid_count


def part_two(filename):
    entries = read_input(filename)

    # Total valid passwords
    valid_count = 0

    for line in entries:
        # Create named groups
        regex = re.match(
            r"(?P<first_position>^\d+)-(?P<second_position>\d+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+$)", line)

        # Variables
        counter = 0
        first_index = int(regex.group('first_position')) - 1
        second_index = int(regex.group('second_position')) - 1

        # Check both positions
        if regex.group('password')[first_index] == regex.group('letter'):
            counter += 1
        if regex.group('password')[second_index] == regex.group('letter'):
            counter += 1

        # Check if ONLY one position is correct
        if counter == 1:
            valid_count += 1

    return valid_count
