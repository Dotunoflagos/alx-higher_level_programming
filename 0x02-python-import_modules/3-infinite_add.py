#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    inputno = len(argv)
    total = 0
    if inputno == 1:
        print('0')
    elif inputno > 2:
        for i in range(1, inputno):
            total = total + int(argv[i])
        print("{:d}".format(total))
