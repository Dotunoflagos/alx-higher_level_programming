#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
# 1. Get the string representation
num_str = repr(n)
# 2. Access the last string of the digit string:
last_digit_str = num_str[-1]
# 3. Convert the last digit string to an integer:
last_digit = int(last_digit_str)
print(f"The last digit of {n} is {last_digit}")