import os


def read_input(filename):
    # Open input file as list
    with open(os.path.abspath(filename)) as input:
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
                c = int(a) * int(b)
                return c


def part_two():
    entries = read_input("input.txt")

    values = []
    for a in entries:
        for b in entries:
            for c in entries:
                check = int(a) + int(b) + int(c)

                if check == 2020:
                    if a not in values:
                        values.append(a)
                    if b not in values:
                        values.append(b)
                    if c not in values:
                        values.append(c)

    # Calculate answer and return value
    d = int(values[0]) * int(values[1]) * int(values[2])
    return d
