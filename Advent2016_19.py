#!/usr/bin/python3

# Initially used brute-force approach to solve core problems
# Resulting solution was O(n^n)
# Ran brute-force for circle sizes 1-100 to identify pattern
# This solution implements the pattern in O(n)

max_size = input("? ")

solution_a = -1
solution_b = 0
b_additive = 1
for circle_size in range(1, max_size + 1):
    solution_a += 2
    if solution_a > circle_size:
        solution_a = 1
    solution_b += b_additive
    if solution_b == circle_size / 2 and circle_size % 2 == 0:
        b_additive = 2
    elif solution_b == circle_size and circle_size < max_size:
        solution_b = 0
        b_additive = 1

print "A:", solution_a
print "B:", solution_b
