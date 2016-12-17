#!/usr/bin/python3


# Flips & reverses the bits in the provided binary number
def flip_bits(bin_num):
    data = []
    for char in bin_num:
        data.insert(0, "1" if char == "0" else "0")
    return "".join(data)


# Get the number of chunks by getting the 2^n number of segments connected by the n-1 dividers
def get_number_of_chunks(chunk_size, target_size):
    num_chunks = 1
    while (num_chunks * chunk_size) + (num_chunks - 1) < target_size:
        num_chunks *= 2
    return num_chunks


# Calculates checksum by looking at the bit pairs in the binary number
# Recursive function - repeats until length is odd
def calc_checksum(bin_num):
    data = []
    index = 0
    while index < len(bin_num):
        char1 = bin_num[index]
        char2 = bin_num[index+1]
        data.append("1" if char1 == char2 else "0")
        index += 2
    calculated = data
    return calculated if len(calculated) % 2 == 1 else calc_checksum(calculated)


a = str(input("? "))
b = flip_bits(a)
disc_length = int(input("? "))
dividers_size = get_number_of_chunks(len(a), disc_length)
solution = [a]

for n in range(1, dividers_size):
    # Using formula from https://en.wikipedia.org/wiki/Dragon_curve
    solution.append("1" if (((n & (-1*n)) << 1) & n) != 0 else "0")
    if n % 2 == 0:
        solution.append(a)
    else:
        solution.append(b)

solution = "".join(solution)[0:disc_length]
checksum = calc_checksum(solution)

print "Checksum:", "".join(checksum)
