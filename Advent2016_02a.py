#!/usr/bin/python3

import sys

x = 1
y = 1
passcode = ""

while True:
    string = sys.stdin.readline()
    if string.__len__() > 1:
        for direction in string:
            if direction == "U":
                y = max(y-1, 0)
            if direction == "D":
                y = min(y+1, 2)
            if direction == "L":
                x = max(x-1, 0)
            if direction == "R":
                x = min(x+1, 2)
        passcode += str(1+(3*y)+x)
    else:
        break

print passcode
