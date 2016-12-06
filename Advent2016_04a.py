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

letters = ""
sectorID = 0
givenChecksum = ""
checksum = ""
sectorSum = 0

while True:
    string = sys.stdin.readline()
    if len(string) > 1:
        parts = re.split("[\W]+", string)
        letters = "".join(parts[0:len(parts)-3])
        sectorID = int(parts[len(parts)-3])
        givenChecksum = parts[len(parts)-2]
        checksum = calcCheckSum(letters)
        if givenChecksum == checksum:
            sectorSum += sectorID
    else:
        break

print sectorSum
