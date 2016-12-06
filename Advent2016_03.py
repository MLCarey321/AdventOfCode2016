#!/usr/bin/python3

import sys


def isValidTriangle(side1, side2, side3):
    # A triangle is valid if the sum of the lengths any two sides is greater than the length of the third
    return int(side1) + int(side2) > int(side3) and int(side1) + int(side3) > int(side2) and int(side2) + int(side3) > int(side1)


sides = [[], [], []]
lineCounter = 0
validCountA = 0
validCountB = 0

while True:
    string = sys.stdin.readline()
    if len(string) > 1:
        sides[lineCounter] = string.split()
        # Part A checks row by row
        if isValidTriangle(sides[lineCounter][0], sides[lineCounter][1], sides[lineCounter][2]):
            validCountA += 1
        lineCounter += 1
        if lineCounter == 3:
            # Part B checks sets of 3 in the same column in consecutive rows
            if isValidTriangle(sides[0][0], sides[1][0], sides[2][0]):
                validCountB += 1
            if isValidTriangle(sides[0][1], sides[1][1], sides[2][1]):
                validCountB += 1
            if isValidTriangle(sides[0][2], sides[1][2], sides[2][2]):
                validCountB += 1
            lineCounter = 0
    else:
        break

print validCountA
print validCountB
