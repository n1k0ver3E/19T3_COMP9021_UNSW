# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 7


'''
Will be tested with height a strictly positive integer.
'''
from math import sqrt

def f(height):
    '''
    >>> f(1)
    0
    >>> f(2)
     0
    123
    >>> f(3)
      0
     123
    45678
    >>> f(4)
       0
      123
     45678
    9012345
    >>> f(5)
        0
       123
      45678
     9012345
    678901234
    >>> f(6)
         0
        123
       45678
      9012345
     678901234
    56789012345
    >>> f(20)
                       0
                      123
                     45678
                    9012345
                   678901234
                  56789012345
                 6789012345678
                901234567890123
               45678901234567890
              1234567890123456789
             012345678901234567890
            12345678901234567890123
           4567890123456789012345678
          901234567890123456789012345
         67890123456789012345678901234
        5678901234567890123456789012345
       678901234567890123456789012345678
      90123456789012345678901234567890123
     4567890123456789012345678901234567890
    123456789012345678901234567890123456789
    '''
    # Insert your code here
    i = 0
    print(" " * (height-1),end="")
    flag = [x*x for x in range(height)]
    while(i<height * height):
      print(i%10,end="")
      if (i+1) in (flag):
        print("\n",end="")
        print(" " * (height - int(sqrt(i))-2),end="")

      i = i+1



if __name__ == '__main__':
    import doctest
    doctest.testmod()
