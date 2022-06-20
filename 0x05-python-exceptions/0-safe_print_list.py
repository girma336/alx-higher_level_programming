#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for list in range(x):
        try:
            print("{:d}".format(my_list[list]), end="")
            i = i + 1
        except IndexError:
            break
    print("")
    return i
