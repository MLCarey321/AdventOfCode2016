#!/usr/bin/python3

import sys
import re

abba = re.compile(".*([a-z])([a-z])\\2\\1.*", re.I)
notAbba = re.compile(".*\[[^\]]*([a-z])([a-z])\\2\\1[^\[]*\].*", re.I)
char1 = ""
char2 = ""
count = 0

while True:
    string = sys.stdin.readline()
    if len(string) > 1:
        m = abba.match(string)
        n = notAbba.match(string)
        if m and m.group(1) != m.group(2) and not (n and n.group(1) != n.group(2)):
            count += 1
    else:
        break

print count
