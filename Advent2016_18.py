#!/usr/bin/python3

current_row = input("? ")
max_rows = input("? ")
row_length = len(current_row)
safe_count = current_row.count(".")

for row_num in range(1, max_rows):
    next_row = []
    for column in range(0, row_length):
        sides = ["." if column == 0 else current_row[column - 1], "." if column == row_length - 1 else current_row[column + 1]]
        next_row.append("^" if sides.count("^") == 1 else ".")
    safe_count += next_row.count(".")
    current_row = next_row

print safe_count
