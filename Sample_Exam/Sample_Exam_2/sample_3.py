# COMP9021 19T3 - Rachid Hamadi
# Sample Exam 2


'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.

Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).

The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.

'''

import itertools
def check_str(seq):
    res = ""
    for char in seq:
        if char not in res:
            res = res + char
    return res
    
def good_subsequences(word):
    '''
    >>> good_subsequences('')
    ['']
    >>> good_subsequences('aaa')
    ['', 'a']
    >>> good_subsequences('aaabbb')
    ['', 'a', 'ab', 'b']
    >>> good_subsequences('aaabbc')
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> good_subsequences('aaabbaaa')
    ['', 'a', 'ab', 'b', 'ba']
    >>> good_subsequences('abbbcaaabccc')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
    >>> good_subsequences('abbbcaaabcccaaa')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    '''
    # Insert your code here
    seq = ""
    for i in range(len(word)):
        if len(seq) == 0 or word[i] != word[i-1]:
            seq = seq + word[i]
#    print(seq)
    res = list()
    for i in range(len(seq)+1):
        temp = list(itertools.combinations(seq,i))
        for e in temp:
            e = "".join(e)
            e = check_str(e)
            if e not in res:
                res.append(e)
    res = sorted(res)
    print(res)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
