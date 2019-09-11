#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = (abs(number) % 10)
if number < 0:
    lastdigit *= -1
str = "Last digit of {:d} is {:d} ".format(number, lastdigit)
if lastdigit > 5:
    str += "and is greater than 5"
elif lastdigit == 0:
    str += "and is 0"
else:
    str += "and is less than 6 and not 0"
print("{}".format(str))
