#!/usr/bin/python3

import sys

keyMap = {(0, 0): "Invalid",    (1, 0): "Invalid",  (2, 0): "1", (3, 0): "Invalid", (4, 0): "Invalid",
          (0, 1): "Invalid",    (1, 1): "2",        (2, 1): "3", (3, 1): "4",       (4, 1): "Invalid",
          (0, 2): "5",          (1, 2): "6",        (2, 2): "7", (3, 2): "8",       (4, 2): "9",
          (0, 3): "Invalid",    (1, 3): "A",        (2, 3): "B", (3, 3): "C",       (4, 3): "Invalid",
          (0, 4): "Invalid",    (1, 4): "Invalid",  (2, 4): "D", (3, 4): "Invalid", (4, 4): "Invalid"}

x = 0
y = 2
tempx = 0
tempy = 0
passcode = ""

while True:
    string = sys.stdin.readline()
    if string.__len__() > 1:
        for direction in string:
            tempx = x
            tempy = y
            if direction == "U":
                tempy = max(y-1, 0)
            if direction == "D":
                tempy = min(y+1, 4)
            if direction == "L":
                tempx = max(x-1, 0)
            if direction == "R":
                tempx = min(x+1, 4)
            if keyMap[(tempx, tempy)] != "Invalid":
                x = tempx
                y = tempy
        passcode += keyMap[(x, y)]
    else:
        break

print passcode
