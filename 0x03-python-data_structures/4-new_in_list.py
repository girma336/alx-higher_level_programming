#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = []
        for i in my_list:
            if my_list.index(i) == idx:
                new_list.append(element)
            else:
                new_list.append(i)
        return new_list
