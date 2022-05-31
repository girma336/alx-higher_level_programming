#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if num < 0:
    num = -1 * num
if num % 10 == 0:
    print("Last digit of {} is {} and is 0".format(number, num % 10))
elif num% 10 > 5:
    print("Last digit of {} is {} greater than 5".format(number, num % 10))
else:
    if number < 0:
        num = -1 * num
    print("Last digit of {} is {} less than 6 and not zero".format(number, num % 10))
