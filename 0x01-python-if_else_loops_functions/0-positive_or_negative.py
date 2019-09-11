#!/usr/bin/python3
import random
number = random.randint(-10, 10)
str = "{:d} ".format(number)
if number > 0:
    str += "is positive"
elif number == 0:
    str += "is zero"
else:
    str += "is negative"
print("{}".format(str))
