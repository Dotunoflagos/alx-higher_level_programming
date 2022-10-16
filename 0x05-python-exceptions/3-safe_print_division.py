#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resaultz = a/b
        return resaultz
    except (ZeroDivisionError):
        resaultz = None
        return resaultz
    finally:
        print("Inside result: {}".format(resaultz))
