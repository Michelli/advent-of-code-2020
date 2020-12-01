import os
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

    # First loop
    for a in entries:

        # Second loop
        for b in entries:
            check = int(a) + int(b)

            if check == 2020:
                # Calculate answer and return value
                return int(a) * int(b)


def part_two():
    entries = read_input("input.txt")

    values = []
    for a in entries:
        for b in entries:
            for c in entries:
                check = int(a) + int(b) + int(c)

                if check == 2020:
                    # Calculate answer and return value
                    return int(a) * int(b) * int(c)
