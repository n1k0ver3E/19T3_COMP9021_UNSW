# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3

import sys
from random import seed, randrange
from pprint import pprint
from collections import deque

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}
original_mapping = mapping

# INSERT YOUR CODE HERE
def return_circle(mapping):
    for key,value in mapping.items():
        temp = deque()
        temp.append(key)
        temp.append(value)
        if key == value:
            cycles.append([key])
        else:
            while value in list(mapping.keys()):
                temp.append(value)
                temp.append(mapping[value])
                value = mapping[value]
                if temp[0] == temp[-1]:
                    if sorted(list(set(temp))) not in cycles:
                        cycles.append(sorted(list(set(temp))))
                    break
                if len(temp) > len(mapping.items()) * 2:
                    break
    return cycles

def return_reversed(original_mapping):
    result =dict()
    dict1 = dict()
    for i in list(original_mapping.values()):
        result[list(original_mapping.values()).count(i)]={}
    for value in original_mapping.values():
        temp =[]
        for key in original_mapping.keys():
            if value == original_mapping[key]:
                temp.append(key)
        dict1[value] = temp
    for k,v in dict1.items():
        for r in result:
            if len(v) == r:
                result[r][k]=v
    return result

reversed_dict_per_length = return_reversed(original_mapping)
cycles = return_circle(mapping)
cycles.sort()

print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)


