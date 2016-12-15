#!/usr/bin/python3

import sys
import re


def first_start_time(discs):
    start_time = 0
    found = False
    while not found:
        found = True
        for disc in discs:
            if (start_time + disc[0] + disc[2]) % disc[1] != 0:
                found = False
                start_time += 1
                break
    return start_time

info_regex = re.compile("Disc #([\d]*) has ([\d]*) positions; at time=0, it is at position ([\d]*)\.")
data = []

while True:
    disc_info = sys.stdin.readline()
    if len(disc_info) > 1:
        parsed = info_regex.match(disc_info)
        data.append(([int(group) for group in parsed.groups()]))
    else:
        break

print first_start_time(data)
data.append((len(data)+1, 11, 0))
print first_start_time(data)

