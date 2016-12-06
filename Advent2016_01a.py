#!/usr/bin/python3

instructions = input("? ")
x = 0
y = 0
xdiff = 0
ydiff = 1
numdigits = 0
numsteps = 0

route = instructions.split(", ")
for step in route:
    numdigits = len(str(step))
    numsteps = int(step[1:numdigits])
    if step[0] == "R":
        temp = ydiff
        ydiff = -xdiff
        xdiff = temp
    elif step[0] == "L":
        temp = ydiff
        ydiff = xdiff
        xdiff = -temp
    x += (numsteps * xdiff)
    y += (numsteps * ydiff)

print abs(x) + abs(y)
