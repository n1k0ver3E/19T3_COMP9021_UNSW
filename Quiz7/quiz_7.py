# -*- coding: utf-8 -*-
# @Author: Niko
# @Date:   2019-11-11 11:07:16
# @Last Modified by:   Niko
# @Last Modified time: 2019-11-11 15:02:01

from random import seed, randrange
import sys

dim = 10

def display_grid():
    for row in grid:
        print('   ', *row) 

def turn_left(x,y):
  if y == -1 or grid[x][y] ==0:
    return False
  else:
    return ([x,y])
def turn_right(x,y):
  if y==10 or grid[x][y] == 0:
    return False
  else:
    return([x,y])
def turn_down(x,y):
  if x==10 or grid[x][y] == 0:
    return False
  else:
    return ([x,y])
def turn_up(x,y):
  if x== -1 or grid[x][y] == 0:
    return False
  else:
    return ([x,y])
 
def colour_shapes(x,y):
  global min_mark
  mark = 0
  grid[x][y] = flag
  left = turn_left(x,y-1)
  right = turn_right(x,y+1)
  down = turn_down(x+1,y)
  up = turn_up(x-1,y)
  if left:
    mark = mark + 1
    if left not in child and left not in seen  : child.append(left)
  if right :
    mark = mark + 1
    if right not in child and right not in seen : child.append(right)
  if down :
    mark = mark + 1
    if down not in child and down not in seen : child.append(down)
  if up :
    mark = mark + 1
    if up not in child and up not in seen: child.append(up)
  if mark == 1: min_mark = min_mark + 1
  seen.append([x,y])
  if child :
    new = child.pop(0)
    colour_shapes(new[0],new[1])
  else:
    return False

def max_number_of_spikes(nb_of_shapes):
    return max(nb_of_shapes)

try: 
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
flag = 2 # color_index
seen,child=list(),list()
number_of_spikes = list()

for i in range(dim):
  for j in range(dim):
    if grid[i][j] == 1:
        min_mark = 0
        colour_shapes(i,j)
        number_of_spikes.append(min_mark)
        flag = flag +1

print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(number_of_spikes)
     )
