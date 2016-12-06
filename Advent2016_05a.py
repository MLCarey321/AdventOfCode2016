#!/usr/bin/python3

import hashlib

doorID = input("? ")
salt = 1
password = ""

while True:
    string = doorID + str(salt)
    hashed = str(hashlib.md5(string).hexdigest())
    if hashed[0:5] == "00000":
        print "Salt: " + str(salt) + "; Hash: " + hashed
        password += hashed[5]
        if len(password) == 8:
            break
    salt += 1

print password
