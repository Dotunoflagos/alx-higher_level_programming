#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    last = ((num * -1) % 10) * -1
else:
    last = num % 10
if last > 5:
    print('Last digit of {:d} is {:d} and is greater than 5'
          .format(num, last))
elif last == 0:
    print('Last digit of {:d} is {:d} and is 0'.format(num, last))
elif last < 6 and last != 0:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0'
          .format(num, last))
