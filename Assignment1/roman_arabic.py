import re,sys

def get_rule(result,std_count,std_dict):
    rule =""
    index = std_count.index([result.count(k) for k in result]) +1
    ordinary = std_dict[index]
    for i in['C','L','X','V','I']:
        if i in ordinary:
            rule = rule + result[ordinary.index(i)]
        else:
            rule = rule + "_"

    rule = rule.lstrip("_")
    return rule


def return_valid(input):
    for i,v in enumerate(reversed(input)):
        if input.count(v)>=4:
            if input[input.index(v):len(input)-i] == v * 4:
                return True
    return False

def return_norm(string):
    sp_num,sp_str = list(),list()
    for i,v in enumerate (reversed(string),1):   
        if i%2 ==1:
            sp_num.append(10 ** (i//2))
            sp_str.append(v)
        elif i%2 == 0:
            sp_num.append(10 ** (i//2 - 1) * 5)
            sp_str.append(v)
    temp = list(zip(sp_num,sp_str))
    for i in range(1,len(temp)+1):
        if i%2 == 0:
            temp.append((int(temp[i-1][0])-int(temp[i-2][0]),temp[i-2][1]+temp[i-1][1]))
        elif i!=1 and i%2 ==1:
            temp.append((int(temp[i-1][0])-int(temp[i-3][0]),temp[i-3][1]+temp[i-1][1]))
    norm = dict(sorted(temp))

    return norm

def arabic2roman(integer,norm):
    key,value = list(norm.keys()),list(norm.values())
    result = ''
    i = len(norm) - 1
    if integer == 9 and integer not in key: return False
    while (integer > 0):
        while (i >= 0) :
            if integer >= key[i] :
                result = result + value[i]; # append the roman sybol
                integer = integer - key[i]; # subtract the number
            else :
                i = i - 1
    if return_valid(result) == True:
        return False
    else:
        return result
       
def roman2arabic(string,norm):
    key,value = list(norm.keys()),list(norm.values())
    former = int(key[value.index(string[-1])])
    result = 0 + former
    for item in reversed(string[:-1]):
        if key[value.index(item)] >= former:
            result = result + key[value.index(item)] 
        elif key[value.index(item)] < former:
            result = result - key[value.index(item)]
        former = key[value.index(item)]

    if string == arabic2roman(result,norm):
        return result
    else:
        return False

def first_kind(input):
    general_num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    general_str = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    norm = dict(zip(general_num,general_str))
    if input.isdigit() and input[0] is not '0' and int(input)<4000 and int(input)>0 and arabic2roman(int(input),norm):
        print("Sure! It is " + str(arabic2roman(int(input),norm)))
    elif input.isalpha() and roman2arabic(input,norm):
        print("Sure! It is " + str(roman2arabic(input,norm)))
    else:
        print("Hey, ask me something that's not impossible to do!")

def second_kind(input,string):
    norm = return_norm(string)
    if input.isdigit() and input[0] is not '0' and int(input)>0 and arabic2roman(int(input),norm):
        print ("Sure! It is " + arabic2roman(int(input),norm))
    elif input.isalpha() and not False in list(map(lambda r:r in string,[i for i in input])) and roman2arabic(input,norm):
        print ("Sure! It is " + str(roman2arabic(input,norm)))
    else:
        print ("Hey, ask me something that's not impossible to do!")

def third_kind(input):
    if True in list(map(lambda x:x.isdigit(),[i for i in input])):
        return ("Hey, ask me something that's not impossible to do!")
    temp = ""
    temp_list,std_count,result = list(),list(),list()
    general_num,general_str = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000],["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    norm = dict(zip(general_num,general_str))
    std_dict = dict()
    for i in range(1,101):
        std_dict[i] = arabic2roman(i,norm)
    # print(std_dict)
    for i in range(1,len(std_dict)):
        str1 = std_dict[i]
        use = [str1.count(k) for k in str1]
        std_count.append(use)
    # print(std_count)

    for i,v in enumerate(reversed(input)):
        if input.count(v) >1:
            first = input.index(v)
            circle = input[first:len(input)-i]
            # print(circle)
            if [circle.count(k) for k in circle] in std_count:
                if [(circle+temp).count(k) for k in (circle+temp)] in std_count:
                    temp = v + temp
                else:
                    result.append(temp)
                    temp = v
                    continue
            else:
                return("Hey, ask me something that's not impossible to do!")
        else : 
            temp = v + temp

        if [temp.count(k) for k in temp] in std_count:
            pass
        else:
            result.append(temp[1:])
            temp = v
    result.append(temp)

    for i in range(len(result)):
        flag=0
        if i == 0:
            rule = get_rule(result[i],std_count,std_dict)
        else:
            temp = get_rule(result[i],std_count,std_dict)
            if temp[-1] == rule[0]:
                com = rule.index("_")
                rule = rule[:com] +rule[com+1:]
                rule = rule[1:]
            for t in temp:
                if input.count(t)>1:
                    blah = len(temp)-temp.index(t)+len(rule)
                    if blah%2==1:
                        flag = 0
                    else:
                        flag = 1
            if flag ==1 :
                rule = temp + "_" + rule
            else:
                rule = temp + rule


    norm = return_norm(rule)
    v = list(norm.values())
    if False in list(map(lambda x: x in v,[i for i in input])):
        return ("Hey, ask me something that's not impossible to do!")
    num = str(roman2arabic(input,norm))
    if num == str(False) :
        return ("Hey, ask me something that's not impossible to do!")
    else:
        return ("Sure! It is " + num + " using " + rule)
try:
    text = (input("How can I help you? ")).split(" ")
    if text[0]=="Please" and text[1]=="convert" and len(text) == 3:
        first_kind(text[2])
    elif text[0]=="Please" and text[1]=="convert" and len(text) == 5 and text[3] == "using":
        second_kind(text[2],text[4])
    elif text[0]=="Please" and text[1]=="convert" and len(text) == 4 and text[3] == "minimally":
        print(third_kind(text[2]))
    else:
        raise IOError

except IOError:
    print("I don't get what you want, sorry mate!")
    sys.exit()