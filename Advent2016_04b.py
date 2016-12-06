#!/usr/bin/python3

import sys
import re
from operator import itemgetter


def calcCheckSum(letters):
    letterCounts = set()
    for letter in letters:
        letterCounts.add((letter, letters.count(letter)))
    letterList = sorted(list(letterCounts), key=itemgetter(0))
    letterList = sorted(letterList, key=itemgetter(1), reverse=True)
    return "".join([letter[0] for letter in letterList][0:5])

cipher = "abcdefghijklmnopqrstuvwxyz"
decoded = []
roomName = ""

letters = ""
sectorID = 0
givenChecksum = ""
checksum = ""
shiftAmount = 0

while True:
    string = sys.stdin.readline()
    if len(string) > 1:
        parts = re.split("[\W]+", string)
        letters = "".join(parts[0:len(parts)-3])
        sectorID = int(parts[len(parts)-3])
        givenChecksum = parts[len(parts)-2]
        checksum = calcCheckSum(letters)
        if givenChecksum == checksum:
            decoded = []
            shiftAmount = sectorID % 26
            for char in string:
                if char in cipher:
                    decoded.append(cipher[(cipher.index(char) + shiftAmount) % 26])
                elif char == "-":
                    decoded.append(" ")
                else:
                    break
            roomName = "".join(decoded)
            if "north" in roomName and "pole" in roomName:
                print "Message for Sector ID `" + str(sectorID) + "`: " + "".join(decoded)
    else:
        break
