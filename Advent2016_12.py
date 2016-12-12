#!/usr/bin/python3

import sys
import re

instructions = []
registers = {}


def set_register_value(r, v):
    if r not in registers.keys():
        registers.keys().append(r)
    registers[r] = v


def get_register_value(r):
    if r not in registers.keys():
        return 0
    return registers[r]


def get_test_value(input):
    if re.match("\d", input):
        return int(input)
    return get_register_value(input)


while True:
    line = sys.stdin.readline()
    if len(line) > 1:
        instructions.append(line)
    else:
        break

index = 0

# Setting register "c" to 1 as per part 2 instructions - comment out to get part A solution
set_register_value("c", 1)
while index < len(instructions):
    parts = instructions[index].split()
    instruction = parts[0]
    if "cpy" == instruction:
        value = get_test_value(parts[1])
        register = parts[2]
        set_register_value(register, value)
        index += 1
    elif "inc" == instruction:
        register = parts[1]
        value = get_register_value(register)
        set_register_value(register, value + 1)
        index += 1
    elif "dec" == instruction:
        register = parts[1]
        value = get_register_value(register)
        set_register_value(register, value - 1)
        index += 1
    elif "jnz" == instruction:
        value = get_test_value(parts[1])
        if value == 0:
            index += 1
        else:
            index += int(parts[2])

print registers["a"]
