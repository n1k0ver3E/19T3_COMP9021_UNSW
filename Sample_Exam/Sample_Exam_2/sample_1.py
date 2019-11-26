# COMP9021 19T3 - Rachid Hamadi
# Sample Exam 2


def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)               
    result = ""
    if word=="":
        result = word
    else:
        for ch in word:
            if len(result) == 0 or ch != result[-1]:
                result = result + ch
    
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
