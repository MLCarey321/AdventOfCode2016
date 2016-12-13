#!/usr/bin/python3

import sys
from copy import deepcopy

fav_num = input("Designer's Favorite Number? ")
destination = input("Destination Coordinates?    ")
max_steps = input("Maximum Steps?              ")
spaces = {(1, 1): "."}
max_spaces = set()
lowest_found = sys.maxsize


def is_space_open(x, y):
    # Use a cache for performance, look-up as needed
    if (x, y) not in spaces.keys():
        spaces.keys().append((x, y))
        spaces[(x, y)] = get_space_contents(x, y)
    return "." == spaces[(x, y)]


def get_space_contents(x, y):
    # Use provided formula to determine open (".") or wall ("#")
    global fav_num
    calc = x * x + 3 * x + 2 * x * y + y + y * y + fav_num
    binary = str(bin(calc)[2:])
    return "." if 0 == binary.count("1") % 2 else "#"


def is_valid_coordinates(x, y, traversed=[]):
    # Coordinates must be non-negative, open spaces that have not already been traversed on this specific path
    return x >= 0 and y >= 0 and (x, y) not in traversed and is_space_open(x, y)


def get_minimum_route(current_x, current_y, traversed=[], steps=0):
    global lowest_found, max_spaces, max_steps
    if steps <= max_steps:
        max_spaces.add((current_x, current_y))
    if (current_x, current_y) == destination:
        # Update the "Lowest Found" value, if applicable
        lowest_found = min(lowest_found, steps)
        if steps >= max_steps:
            # If we've hit our max steps and reached our destination, no point in going further
            return steps
    elif steps >= max_steps and steps >= lowest_found > 0:
        # Short-circuit if we know we're not going to get lower than we've already found
        # and we've already hit our max steps for part B
        return sys.maxsize
    # Use a deep copy to prevent false positives when checking already-visited coordinates
    copy_traversed = deepcopy(traversed)
    copy_traversed.append((current_x, current_y))
    possibilities = []
    # Check all 4 possibilities, return the lowest
    if is_valid_coordinates(current_x+1, current_y, copy_traversed):
        possibilities.append(get_minimum_route(current_x + 1, current_y, copy_traversed, steps + 1))
    if is_valid_coordinates(current_x, current_y+1, copy_traversed):
        possibilities.append(get_minimum_route(current_x, current_y + 1, copy_traversed, steps + 1))
    if is_valid_coordinates(current_x-1, current_y, copy_traversed):
        possibilities.append(get_minimum_route(current_x - 1, current_y, copy_traversed, steps + 1))
    if is_valid_coordinates(current_x, current_y-1, copy_traversed):
        possibilities.append(get_minimum_route(current_x, current_y - 1, copy_traversed, steps + 1))
    # If no new possibilities were found, return sys.maxsize
    return min(possibilities) if possibilities else sys.maxsize


def print_map():
    for y in range(0, max(space[1] for space in spaces.keys())):
        line = ""
        for x in range(0, max(space[0] for space in spaces.keys())):
            if (x, y) in spaces:
                line += spaces[(x, y)]
            else:
                line += " "
        print line

get_minimum_route(1, 1)
print lowest_found
print len(max_spaces)
# print_map()
