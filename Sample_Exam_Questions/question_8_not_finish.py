# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 8


'''
Will be tested with letters a string of DISTINCT UPPERCASE letters only.
'''

def count_str(string):
    dic = dict()
    for e in string:
        dic[e] = string.count(e)
    return dic


def f(letters):
    '''
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    '''
    dictionary = 'dictionary.txt'
    solutions = []
    result = list()
    new = list()
    with open(dictionary,'r') as f:
        for line in f.readlines():
            if line[0] in sorted(letters):
                result.append(line[:-1])

    for r in result[:]:
        for char in r:
            if char not in letters:
                result.remove(r)
                break
    
    print(result)
    for r in result[:]:
        temp = list(reversed(sorted(letters)))
        for char in reversed(r):
            temp.remove(char)
        print(temp)



    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')
        for solution in solutions:
            print(solution)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
