#!/usr/bin/python3

# O(log(n)) solutions for Day #19

max_size = input("? ")

starting_circle = 1
while starting_circle * 2 < max_size:
    starting_circle *= 2

print "Part 1:", 1 + (2 * (max_size - starting_circle))

starting_circle = 1
while starting_circle * 3 <= max_size:
    starting_circle *= 3

print "Part 2:", starting_circle if starting_circle == max_size else max_size - starting_circle
