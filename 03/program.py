import os
import sys
from math import prod


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

    # Variables
    position = 0
    trees = 0

    for row in entries:
        # Ensure position does not exceed index
        if (position + 1) > len(row):
            # Repeat the row
            position -= len(row)

        # Check if it's a tree
        if row[position] == "#":
            trees += 1

        # Move to the next position
        position += 3

    return trees


def part_two(filename):
    entries = read_input(filename)

    # Running count
    total_trees = []

    for right, down in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
        # Reset counter
        trees = 0

        # Reset position
        position = 0

        for row in enumerate(entries[::down]):
            # Ensure position does not exceed index
            if (position + 1) > len(row[1]):
                # Repeat the row
                position -= len(row[1])

            # Check if it's a tree
            check = row[1][position]
            if row[1][position] == "#":
                trees += 1

            # Move to the next position
            position += right

        total_trees.append(trees)

    return prod(total_trees)
