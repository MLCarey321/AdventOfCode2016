#!/usr/bin/python3

import sys


def most_common(lst):
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]


def least_common(lst):
    return min(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]

lines = []
dataA = []
dataB = []

while True:
    string = sys.stdin.readline()
    if len(string) > 1:
        lines.append(string)
    else:
        break

for index in range(0, len(str(lines[0]))):
    dataA.append(most_common([line[index] for line in lines]))
    dataB.append(least_common([line[index] for line in lines]))

print "".join(dataA)
print "".join(dataB)
