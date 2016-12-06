#!/usr/bin/python3

import hashlib
import re

doorID = input("? ")
salt = 1
password = list("        ")
position = 0

while True:
    string = doorID + str(salt)
    hashed = str(hashlib.md5(string).hexdigest())
    if hashed[0:5] == "00000":
        print "Salt: " + str(salt) + "; Hash: " + hashed
        if re.match("\d", hashed[5]):
            position = int(hashed[5])
            if position < 8 and password[position] == " ":
                password[position] = hashed[6]
                if " " not in password:
                    break
    salt += 1

print "".join(password)
