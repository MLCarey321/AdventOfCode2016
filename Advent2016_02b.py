#!/usr/bin/python3

import sys

keyMap = {(0, 0): " ", (1, 0): " ", (2, 0): "1", (3, 0): " ", (4, 0): " ",
          (0, 1): " ", (1, 1): "2", (2, 1): "3", (3, 1): "4", (4, 1): " ",
          (0, 2): "5", (1, 2): "6", (2, 2): "7", (3, 2): "8", (4, 2): "9",
          (0, 3): " ", (1, 3): "A", (2, 3): "B", (3, 3): "C", (4, 3): " ",
          (0, 4): " ", (1, 4): " ", (2, 4): "D", (3, 4): " ", (4, 4): " "}

x = 0
y = 2
tempx = 0
tempy = 0
passcode = ""

while True:
    string = sys.stdin.readline()
    if len(string) > 1:
        for direction in string:
            tempx = x
            tempy = y
            if direction == "U":
                tempy = max(y-1, 0)
            elif direction == "D":
                tempy = min(y+1, 4)
            elif direction == "L":
                tempx = max(x-1, 0)
            elif direction == "R":
                tempx = min(x+1, 4)
            if keyMap[(tempx, tempy)] != " ":
                x = tempx
                y = tempy
        passcode += keyMap[(x, y)]
    else:
        break

print passcode
