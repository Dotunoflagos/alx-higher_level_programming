#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    inputno = len(argv)
    if inputno == 1:
        print(f'{inputno - 1:d} arguments.')
    else:
        print(f'{inputno - 1} arguments:')
        for i in range(1,inputno):
            print(f"{i:d}: {argv[i]:s}")
