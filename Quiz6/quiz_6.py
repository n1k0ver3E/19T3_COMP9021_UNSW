# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys

dim = 10

def display_grid():
    for row in grid:
        print('   ', *row) 

def size_of_largest_parallelogram(left,right,rectangle):
  return max(left,right,rectangle)


def left_parallelogram(i,j):
  if i + 1 > 9 or j - 2 < 0: return (i,j)
  if grid[i][j] == 1 and grid[i][j-1] == 1 and grid[i+1][j-1] == 1 and grid[i+1][j-2] ==1:
    return left_parallelogram(i+1,j-1)
  else:
    return (i,j)

def right_parallelogram(i,j):
  if i + 1 > 9 or j + 2 > 9: return (i,j)
  if grid[i][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j+1] ==1 and grid[i+1][j+2] == 1:
    return right_parallelogram(i+1,j+1)
  else:
    return (i,j)

def get_left_area(temp,length):
  i = ox
  cj = oy
  while (i<=9):
    for j in range(cj,cj-length,-1):
      if grid[i][j]!=1:
        temp = (i-ox) * length
        if cj - j < 2: return temp
        else:
          length = cj - j
          return get_left_area(temp , length)
      else:
        pass
    area = (i-ox) * length  
    if temp > area:
      area = temp
    else:
      pass
    i = i + 1
    cj = cj - 1
    if cj < 0 : return area
  return area



def get_right_area(area,length):
  i = ox
  cj = oy
  while (i<=9):
    if cj+length >9: length = length -1
    for j in range(cj,cj+length):
      if grid[i][j] != 1:
        if (i - ox) ==1:
          temp = 0
        else:
          temp = (i-ox) * length
        if temp > area:
          area = temp

        if j- cj <2:
          return area
        else:
          length = j - cj
          get_right_area(area,length)
    i = i + 1
    cj = cj +1
  area = (i-ox) * length
  return area

def get_square(temp,length):
  # print("tips",ox,oy,length,square)
  i = ox
  cj = oy 
  while(i<10):
    for j in range(cj,cj+length):
      if grid[i][j] != 1:
        temp1 = (i-ox) * length
        # print("sfs",j-cj,temp1)
        if j - cj < 2: 
          if temp> temp1:
            return (temp)
          else:
            return temp1
        else:
          length = j - cj
          return get_square(temp1,length)
      else:
        pass
    area = (i-ox) * length
    if temp > area:
      area = temp
    else:
      pass
    i = i + 1
  # print(area)
  temp = (i-ox) * length
  if temp > area:
    return temp
  else:
    return area





  #       print("invalid=",ox,oy,i,j)
  #       temp = (i-ox) * length
  #       print("temparea",temp)
  #       if temp > square :
  #         square = temp
  #       if j - oy <2:
  #         return square
  #         break
  #       else:
  #         length = j - oy
  #         get_square(square,length)
  #   i = i + 1
  # square = (i-ox) * length
  # return square




def isValidRightParallel(i,j):
  if grid[i][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j+1] ==1 and grid[i+1][j+2] == 1:
    return True
  else:
    return False

def isValidLeftParallel(i,j):
  if grid[i][j] == 1 and grid[i][j-1] == 1 and grid[i+1][j-1] == 1 and grid[i+1][j-2] ==1:    
    return True
  else:
    return False

def isValidRect(i,j):
  if grid[i][j] ==1 and grid[i+1][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j+1] == 1:
    return True
  else:
    return False

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

# print(grid)
right,left,rect = 0,0,0
for i in range(9):
  for j in range(8):
    if isValidRightParallel(i,j):
      ox,oy = i,j
      for e in range(j+1,10):
        if grid[i][e] == 0:
          length = e - j
          break
        length = 10 -j
      temp = get_right_area(0,length)
      if right < temp : 
        right = temp

for i in range(9):
  for j in range(2,10):
    if isValidLeftParallel(i,j):
      ox,oy = i,j
      for e in range(j-1,0,-1):
        if grid[i][e] == 0:
          length =  j - e
          break
        length = j
      temp = get_left_area(0,length)
      # print(ox,oy,temp)
      if left < temp:
        left = temp


for i in range(9):
  for j in range(9):
    if isValidRect(i,j):
        ox,oy = i,j
        for e in range(j+1,10):
          if grid[i][e] == 0:
            length = e - j
            break
          length = 10 - j 
        # print(ox,oy,length)
        t = get_square(0,length)
        # print(t)
        if t > rect: rect = t


print('Here is the grid that has been generated:')
display_grid()
# print(left,right,rect)
size = size_of_largest_parallelogram(left,right,rect)
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')
