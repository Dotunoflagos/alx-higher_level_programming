#!/usr/bin/python3
"""
Creates a class inheriting from the list class.
"""


class MyList(list):
    """Inherits from list"""
    
    def print_sorted(self):
        """prints in ascending order"""
    
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
