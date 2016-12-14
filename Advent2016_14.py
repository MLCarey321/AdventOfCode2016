#!/usr/bin/python3

import hashlib
import re

salt = input("? ")
triple = re.compile(".?(.)\\1\\1.*", re.I)
keys = []
index = 0
stretched_hash_cache = {}


def calc_hash(flavor):
    global salt
    return str(hashlib.md5(salt + str(flavor)).hexdigest())


def calc_stretched_hash(flavor):
    global salt, stretched_hash_cache
    if flavor not in stretched_hash_cache.keys():
        stretched_hash_cache.keys().append(flavor)
        stretched = calc_hash(flavor)
        for x in range(0, 2016):
            stretched = str(hashlib.md5(stretched).hexdigest())
        stretched_hash_cache[flavor] = stretched
    else:
        stretched = stretched_hash_cache[flavor]
    return stretched


def has_five_hash(starting_index, repeating_char):
    fiver = re.compile(".*("+(repeating_char*5)+").*", re.I)
    # print fiver.pattern
    for delta in range(1, 1001):
        five_hash = calc_stretched_hash(starting_index+delta)
        if fiver.match(five_hash):
            # print repeating_char, delta, five_hash
            return True
    return False

while len(keys) < 64:
    hashed = calc_stretched_hash(index)
    matched = triple.search(hashed)
    if matched:
        char = matched.group(1)
        # print "Potential Key Found", hashed
        # print "Triple Character", char
        if has_five_hash(index, char):
            print "Key Found!", index, hashed
            keys.append(hashed)
    index += 1

print index-1, keys[63]
