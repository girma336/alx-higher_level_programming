#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary == {}:
        return None
    del_key = []
    for k, v in a_dictionary.items():
        if v == value:
            del_key.append(k)
    for i in del_key:
        del a_dictionary[i]
    return a_dictionary
