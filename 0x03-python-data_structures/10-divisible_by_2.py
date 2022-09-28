#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    answer, i = [], 0
    if my_list:
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                answer.append(True)
            elif my_list[i] % 2 == 1:
                answer.append(False)
        return answer