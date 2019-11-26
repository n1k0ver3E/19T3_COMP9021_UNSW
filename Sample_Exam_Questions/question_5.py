# -*- coding: utf-8 -*-
# @Author: Niko
# @Date:   2019-11-10 15:13:29
# @Last Modified by:   Niko
# @Last Modified time: 2019-11-26 15:04:17
# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 5


'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''


import csv

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    arr_d,arr_i,arr_f = list(),list(),list()
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    path ="/Users/Niko/Temp/cpiai.csv"      # absolute path for the csv file
    path = 'cpiai.csv'

    with open (path,newline="") as file:
        content = csv.reader(file)    # get all the lines from the file
        for row in content:         # get each line from content variable
            if (row[0][0:4] == str(year)):
                arr_d.append(row[0][5:7])       # extract the year
                arr_i.append(row[1])            # extract the index
                arr_f.append(row[2])            # extract the Inflation
    max = [(-1,min(arr_f))]     # initerate the max variable with the minimum value
    for i, v in enumerate(arr_f):
        if v>max[0][1]:   # there are 2 circumstance that we have to focus: 1.value is more than max, 2.value is equal to max
            max = [(i,v)]
        elif v ==max[0][1]:
            max.append((i,v))

    result = list()
    for i in max:       # format the output
        result.append(months[int(arr_d[i[0]]) - 1])

    print("In %s, maximum inflation was: %s" %(year,max[0][1]))
    print("It was achieved in the following months: " + ', '.join(result))




if __name__ == '__main__':
    import doctest
    doctest.testmod()
