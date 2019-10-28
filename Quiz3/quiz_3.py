# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys
import numpy as np

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
rec = ('0' * nb_of_leading_zeroes + f'{int(code):o}')
print(rec)
result=[[0,0]]
matrix = np.array([[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]])
temp = np.array([0,0])
rec = reversed(rec)
for i in rec:
    temp = temp + matrix[int(i)]
    if list(temp) in result:
        result.remove(list(temp))
    else:
        result.append(list(temp))
origin = np.array([0,0])

print(result)

if len(result):
    min_res = np.min(result,axis=0)[0], np.min(result,axis=0)[-1]
    print(min_res)
    if min_res != list(origin):
        distance = list(origin - np.array(min_res))
    else:
        distance = origin

    for i in range (len(list(result))):
        result[i] = list(np.array(distance) + np.array(result[i]))

    print(result)
    cols,rows = np.max(result,axis=0)[0]+1, np.max(result,axis=0)[-1]+1
    # new =  [[off for row in range(rows)] for col in range(cols)]
    new=list()
    for col in range(cols):
        new.append([off]*rows)

    for item in result:
        new[item[0]][item[1]]=on

    new = np.array(new).transpose()
    for i in reversed(range(len(new))):
        for k in range(len(new[i])):
            print(new[i][k], end="")
        print("\n")
else:
    print("")


