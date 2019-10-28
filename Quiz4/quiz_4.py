# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys

def return_valid_symbol(string):
    if string == " ":
        return False
    string = string.strip()
    for letter in string:
        if letter.isalpha() or letter =="_":
            continue
        else:
            return False
    return True

def is_valid(word, arity):
    if arity == 0:
        return return_valid_symbol(word)
    else:
        stack =list()
        temp=""
        if "(" and ")" not in word: 
            return False
        else:
            for letter in word:
                if letter =="(":
                    if len(temp) and return_valid_symbol(temp):
                        temp = temp+"("
                        stack.append(temp)
                        temp = ""
                    else: return False
                elif letter.isalpha() or letter =="_" or letter ==" ":
                    temp = temp + letter
                elif letter ==",":
                    if len(temp) and return_valid_symbol(temp):
                        stack.append(temp)
                        temp = ""
                    else: return False
                elif letter ==")":
                    if len(temp) and return_valid_symbol(temp):
                        temp = temp
                        stack.append(temp)
                        tstack = list(reversed(stack))
                        for i in (tstack):
                            if i[-1] =='(':
                                index = -(tstack.index(i)+1)
                                break
                        else:
                            return False
                        if len(stack[index+1:]) == arity: 
                            for i in reversed(stack):
                                if i[-1] =="(":
                                    break
                                stack.pop()
                            stack.pop()
                            temp = "T"
                        else:
                            return False      
                else:
                    return False
            if not len(stack):
                return True
            else:
                return False

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')



