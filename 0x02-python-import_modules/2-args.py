#!/usr/bin/python3
from sys import argv
inputno = len(argv)
if inputno == 1:
    print(f'{inputno - 1} arguments.')
else:
    print(f'{inputno - 1} arguments:')
    for i in range(1,inputno):
        print(f"{i}: {argv[i]}")
    argv[i]
