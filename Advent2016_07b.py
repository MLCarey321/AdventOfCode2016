#!/usr/bin/python3

import sys
import re

# (.*[\[].*[\]])* == Any number of optional blocks, both inside and outside of square brackets
# ([a-z])([a-z])\\2 == 'aba' pattern outside of square brackets
# .* == any amount of characters later
# \[[^\]]* == An opening square bracket followed by any number of characters within the same square bracket section
# \\3\\2\\3 == 'bab' pattern inside of square brackets
# .* == any amount of characters remaining
aba = re.compile("(.*[\[].*[\]])*[^\[]*([a-z])([a-z])\\2.*[\[][^\]]*\\3\\2\\3.*", re.I)

# .* == Any number of characters before matching square bracket section
# \[[^\]]* == An opening square bracket followed by any number of characters within the same square bracket section
# ([a-z])([a-z])\\1 == 'bab' pattern inside of square brackets
# .*\] == The conclusion of the square bracket section
# (.*[\[].*[\]])* == Any number of optional blocks, both inside and outside of square brackets
# [^\[]* == A block outside of square brackets
# \\2\\1\\2 == 'aba' pattern outside of square brackets
# .* == any amount of characters remaining
bab = re.compile(".*\[[^\]]*([a-z])([a-z])\\1.*\](.*[\[].*[\]])*[^\[]*\\2\\1\\2.*", re.I)
count = 0

while True:
    string = sys.stdin.readline()
    if len(string) > 1:
        m = aba.match(string)
        n = bab.match(string)
        if (m and m.group(3) != m.group(2)) or (n and n.group(1) != n.group(2)):
            count += 1
    else:
        break

print count
