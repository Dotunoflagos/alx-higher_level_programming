#!/usr/bin/python3
def weight_average(my_list=[]):
    add = 0
    add2 = 0
    mul = 1
    for i in my_list:
        del mul
        mul = 1
        for j in i:
            mul *= j
        add += mul
        
    for i in my_list:
        add2 += i[1]
        
    return(add/add2)
