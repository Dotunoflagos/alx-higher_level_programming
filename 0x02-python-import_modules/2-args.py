#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    
    inputno = len(argv)
    if inputno == 1:
        print('0 arguments.')
    elif inputno == 2:
        print('1 arguments:')
        print('1: {:s}'.format(argv[1]))
    elif inputno > 2:
            print('{:d} arguments:'.format(inputno - 1))
            for i in range(1,inputno):
                print("{:d}: {:s}".format(i, argv[i]))
