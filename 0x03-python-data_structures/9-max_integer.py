#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        i = 0
        temp = 0
        length = len(my_list)
        while i < length:
            if temp <= my_list[i]:
                temp = my_list[i]
            else:
                temp = temp
            i = i + 1
        return temp
