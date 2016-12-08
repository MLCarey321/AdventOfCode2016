#!/usr/bin/python3

import sys

screen = [list(".................................................."),
          list(".................................................."),
          list(".................................................."),
          list(".................................................."),
          list(".................................................."),
          list("..................................................")]


def lightPixels(y, x):
    for pix in range(0, x):
        for piy in range(0, y):
            screen[pix][piy] = "#"


def rotateColumn(colNum, shiftAmt):
    column = [line[colNum] for line in screen]
    for i in range(0, 6):
        screen[i][colNum] = column[(i + 6 - shiftAmt) % 6]


def rotateRow(rowNum, shiftAmt):
    row = list(screen[rowNum])
    for i in range(0, 50):
        screen[rowNum][i] = row[(i+50-shiftAmt) % 50]

def printScreen():
    for line in screen:
        print "".join(line)

while True:
    string = sys.stdin.readline()
    if len(string) > 1:
        instruction = string.split()
        if instruction[0] == "rect":
            coords = instruction[1].split("x")
            lightPixels(int(coords[0]), int(coords[1]))
        elif instruction[0] == "rotate":
            rowCol = int(instruction[2][2:])
            shiftAmt = int(instruction[4])
            if instruction[1] == "row":
                rotateRow(rowCol, shiftAmt)
            elif instruction[1] == "column":
                rotateColumn(rowCol, shiftAmt)
    else:
        break

count = 0
for line in screen:
    count += line.count("#")
print count
printScreen()
