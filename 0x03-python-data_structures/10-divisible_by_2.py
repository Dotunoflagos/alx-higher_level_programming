#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    answer = []
    j = 0
    if my_list:
        for i in my_list:
            if i % 2 == 0:
                answer[j] = 'True'
                j += 1
            else:
                answer[j] = 'False'
                j += 1
