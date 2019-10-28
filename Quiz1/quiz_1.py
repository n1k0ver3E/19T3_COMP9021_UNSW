# COMP9021 19T3 - Rachid Hamadi
# Quiz 1 *** Due Thursday Week 2


import sys
from random import seed, randrange


try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []

# INSERT YOUR CODE HERE

def return_nonkeys(upper_bound,mapping):
    for i in range(1,upper_bound):
        if i not in list(mapping.keys()):
            nonkeys.append(i)

    return nonkeys

def return_none(upper_bound,mapping):
    length = upper_bound
    for i in range(length):
        mapping_as_a_list.append(mapping.get(i))

    return mapping_as_a_list

def return_one_to_one(mapping):
    temp = []
    mapping_list = list(mapping.items())
    values_list = list(mapping.values())
    for i in range(0,len(values_list)):
        if (values_list.count(values_list[i])) != 1:
            temp.append(i)
    for index in sorted(temp, reverse = True):
        del mapping_list[index]

    return dict(mapping_list)


nonkeys = return_nonkeys(upper_bound,mapping)
mapping_as_a_list = return_none(upper_bound,mapping)
one_to_one_part_of_mapping = return_one_to_one(mapping)

print()
print('EDIT THIS PRINT STATEMENT')
print('The mappings\'s so-called "keys" make up a set whose number of elements is ' + str(len(list(mapping.items())))+".")
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                                      for key in sorted(one_to_one_part_of_mapping)
                             }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)


