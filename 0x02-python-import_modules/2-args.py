#!/usr/bin/python3
from this import d


if __name__ == '__main__':
    from sys import argv
    inputno = len(argv)
    if inputno == 1:
        print(f'{inputno - 1:d} arguments.')
    elif inputno == 2:
        print('1 arguments:')
        print(f"1: {argv[1]:s}")
    elif inputno > 2:
            print(f'{inputno - 1:d} arguments:')
            for i in range(1,inputno):
                print(f"{i:d}: {argv[i]:s}")
