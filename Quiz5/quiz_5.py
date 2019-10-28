# COMP9021 19T3 - Rachid Hamadi
# Quiz 5 *** Due Thursday Week 7
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys


def encode(list_of_integers):
    # print(list_of_integers)
    result = ""
    for item in list_of_integers:
        bin_item = bin(item)[2:]
        for e in bin_item:
            result = result + str(e)*2
        result = result +'0'
    result = result[:-1]
    return int(result,2)


def decode(integer):
    temp = ""
    result = list()
    str1 = str(bin(integer)[2 :])
    i = 0
    if len(str1)==1:return None
    while(True):
        try:
            if(str1[i] == str1[i+1]):
                temp = temp + str1[i]
                i = i + 2
            elif str1[i]!=str1[i+1] and str1[i]=='0':
                result.append(temp)
                temp=""
                i = i + 1
            else:
                return None
        except IndexError:
            return None

        if i >= len(str1):
            break
    result.append(temp)
    
    return [int(e,2) for e in result]


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))
