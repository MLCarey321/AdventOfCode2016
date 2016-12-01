#!/usr/bin/python3

instructions = input("? ")
stops = set()
x = 0
y = 0
xdiff = 0
ydiff = 1
temp = 0
stop = ()
numdigits = 0
numsteps = 0
found = False

route = instructions.split(", ")
stops.add((x, y))
for step in route:
    numdigits = str(step).__len__()
    numsteps = int(step[1:numdigits])
    if step[0] == "R":
        temp = ydiff
        ydiff = -xdiff
        xdiff = temp
    elif step[0] == "L":
        temp = ydiff
        ydiff = xdiff
        xdiff = -temp
    for inc in range(0, numsteps):
        x += xdiff
        y += ydiff
        stop = (x, y)
        if stop in stops:
            print stop
            found = True
            break
        stops.add(stop)
    if found:
        break
