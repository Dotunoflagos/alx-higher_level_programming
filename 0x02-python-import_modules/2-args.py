#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    inputno = len(argv)
    if inputno == 1:
        print(f'{inputno - 1} arguments.')
    elif inputno == 2:
        print(f'{inputno - 1} arguments:')
        for i in range(1,inputno):
            print(f"{i}: {argv[i]}")
    elif inputno > 2:
            print(f'{inputno - 1} arguments:')
            for i in range(1,inputno):
                print(f"{i}: {argv[i]}")
