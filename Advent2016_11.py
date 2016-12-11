#!/usr/bin/python3

from copy import deepcopy
from collections import defaultdict
from itertools import permutations

# initialize floors with Part A input
floors = [[('thulium', 'generator'), ('thulium', 'microchip'), ('plutonium', 'generator'), ('strontium', 'generator')], [('plutonium', 'microchip'), ('strontium', 'microchip')], [('promethium', 'generator'), ('promethium', 'microchip'), ('ruthenium', 'generator'), ('ruthenium', 'microchip')], []]


# Floor is safe if it's empty or doesn't have any generators without a matching microchip
def safe_floor(floor):
    if not floor:
        return True

    stuff = defaultdict(list)
    for item in floor:
        stuff[item[0]].append(item[1])

    #print "Analyzing if floor is safe", floor
    safe = len(set(map(lambda object: 'microchip' in object, [isotope for index, isotope in stuff.iteritems() if len(isotope) == 1]))) < 2
    #print "Floor is safe?", safe
    return safe


def same_floors(f1, f2):
    return [sorted(floor) for floor in f1] == [sorted(floor) for floor in f2]


def check_permutation(current_floors, previous_floors, perm, floor_number, steps, diff):
    #print "Analyzing", perm, "-->", list(perm)
    copy_floors = deepcopy(current_floors)
    # Using list(perm) to transform tuple permutations to lists
    if safe_floor(current_floors[floor_number + diff] + list(perm)):
        map(copy_floors[floor_number].remove, perm)
        #print "Removed", perm
        if safe_floor(copy_floors[floor_number]):
            copy_floors[floor_number + diff] += list(perm)
            if not same_floors(copy_floors, previous_floors):
                #print perm, 'changing floors by diff', diff
                if process_floor(copy_floors, current_floors, floor_number + diff, steps + 1):
                    return True
    return False


def check_permutation_up(current_floors, previous_floors, perm, floor_number, steps):
    return check_permutation(current_floors, previous_floors, perm, floor_number, steps, 1)


def check_permutation_down(current_floors, previous_floors, perm, floor_number, steps):
    return check_permutation(current_floors, previous_floors, perm, floor_number, steps, -1)


def process_floor(current_floors, previous_floors, floor_number=0, steps=0):
    #print "Processing floor ", floor_number, current_floors[floor_number]
    if floor_number == 3 and not current_floors[0] and not current_floors[1] and not current_floors[2]:
        #print 'Done!'
        #print current_floors
        print steps
        return True
    if floor_number < 3:
        for perm in permutations(current_floors[floor_number], 2):
            # First try to bring two items up
               if check_permutation_up(current_floors, previous_floors, perm, floor_number, steps):
                return True
        for perm in current_floors[floor_number]:
            # Then try to bring one item up
            if check_permutation_up(current_floors, previous_floors, [perm], floor_number, steps):
                return True
    if floor_number >= 0:
        for perm in current_floors[floor_number]:
            # If you can't bring items up, try to bring one item down
            if check_permutation_down(current_floors, previous_floors, [perm], floor_number, steps):
                return True
        for perm in permutations(current_floors[floor_number], 2):
            # If you can't bring one item down, try to bring two items down
            if check_permutation_down(current_floors, previous_floors, perm, floor_number, steps):
                return True
    return False


process_floor(floors, floors)

floors[0] += [['elerium', 'generator'],
              ['elerium', 'microchip'],
              ['dilithium', 'generator'],
              ['dilithium', 'microchip']]

process_floor(floors, floors)
