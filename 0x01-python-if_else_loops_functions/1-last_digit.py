#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
n = number % 10
if num < 0:
    num = -1 * num
    n = -(num % 10)
if n == 0:
    print("Last digit of {} is {} and is 0".format(number, n))
elif n > 5:
    print("Last digit of {} is {} greater than 5".format(number, n))
else:
    print("Last digit of {} is {} less than 6 and not zero".format(number, n))
