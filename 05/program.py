import os
import sys
import math


def read_input(filename):
    # Open input file as list
    with open(os.path.join(sys.path[0], filename)) as input:
        entries = input.read().splitlines()
    # Close input.txt
        input.close()
    # Return list
    return entries


def part_one(filename):
    tickets = read_input("input.txt")
    seat_ids = []

    for line in tickets:
        rows = [0, 127]
        column = [0, 7]

        for letter in line:

            if letter == "F":
                rows[1] = math.floor(rows[1] - abs(rows[0] - rows[1]) / 2)
            elif letter == "B":
                rows[0] = math.ceil(rows[1] - abs(rows[0] - rows[1]) / 2)
            elif letter == "L":
                column[1] = math.floor(
                    column[1] - abs(column[0] - column[1]) / 2)
            elif letter == "R":
                column[0] = math.ceil(
                    column[1] - abs(column[0] - column[1]) / 2)

        seat_ids.append(rows[0] * 8 + column[0])

    return max(seat_ids)
