#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        i = 0
        resault = []
        while i < list_length:
            try:
                resault.append(my_list_1[i]/my_list_2[i])
                i += 1
            except ZeroDivisionError:
                print("division by 0")
                resault.append(0)
                i += 1
            except TypeError:
                print("wrong type")
                resault.append(0)
                i += 1
            except IndexError:
                print("out of range")
                resault.append(0)
                i += 1
        return resault
    finally:
        return resault
