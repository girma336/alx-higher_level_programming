#!/usr/bin/python3
def print_last_digit(number):
    num = number
    if num < 0:
        num = -num
    digit = num % 10
    print("{}".format(digit), end="")
    return digit
