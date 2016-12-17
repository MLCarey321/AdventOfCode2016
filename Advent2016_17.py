#!/usr/bin/python3

import hashlib
import sys

passcode = input("? ")
shortest_path = ""
longest_path_size = 0


def shortest_known_path_length():
    return len(shortest_path) if len(shortest_path) > 0 else sys.maxsize


def find_paths(x=0, y=0, current_path=""):
    global passcode, shortest_path, longest_path_size
    if x == y == 3:
        # If we've reached the vault, check to see if we've found our shortest path
        if len(current_path) < shortest_known_path_length():
            shortest_path = current_path
        # Update our longest path size, if applicable
        longest_path_size = max(longest_path_size, len(current_path))
        return
    # Get the hash and pursue valid possible paths
    hashed = str(hashlib.md5(passcode + current_path).hexdigest())
    if y > 0 and hashed[0] in "bcdef":
        find_paths(x, y-1, current_path + "U")
    if y < 3 and hashed[1] in "bcdef":
        find_paths(x, y+1, current_path + "D")
    if x > 0 and hashed[2] in "bcdef":
        find_paths(x-1, y, current_path + "L")
    if x < 3 and hashed[3] in "bcdef":
        find_paths(x+1, y, current_path + "R")

find_paths()
print "Shortest Path:       ", shortest_path
print "Longest Path Length: ", longest_path_size
