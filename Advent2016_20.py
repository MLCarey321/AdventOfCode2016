#!/usr/bin/python3

import sys

blocked = []

while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        parts = line.split("-")
        blocked.append((int(parts[0]), int(parts[1])))
    else:
        break

sorted_blocked = sorted(blocked, key=lambda tup: tup[1])

lowest = 0
for blocked_range in sorted_blocked:
    if lowest in range(blocked_range[0], blocked_range[1] + 1):
        lowest = blocked_range[1] + 1
    else:
        break

print "Part 1:", lowest

sorted_blocked = sorted(blocked, key=lambda tup: tup[0])

total, current_max = sorted_blocked[0]
for blocked_range in sorted_blocked:
    if blocked_range[0] > current_max + 1:
        total += blocked_range[0] - current_max - 1
    current_max = max(current_max, blocked_range[1])

allowed_count = 4294967295 - current_max + total

print "Part 2:", allowed_count
