#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        j = 0
        k = 0
        for a in my_list[:x]:
            try:
                print("{:d}".format(my_list[j]), end="")
                j += 1
                k += 1
            except (ValueError, TypeError):
                j += 1
        if x > j:
            raise IndexError("list index out of range")
        print("\n", end="")
        return k
    except (ValueError, TypeError):
        for a in my_list[j:]:
            try:
                print("{:d}".format(my_list[j]), end="")
                j += 1
                k += 1
            except (ValueError, TypeError):
                j += 1
        print("\n", end="")
        return k



my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))