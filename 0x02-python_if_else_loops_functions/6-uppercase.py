#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (c>='a' or  c>='z'):
            c = chr(ord(c)-32)
        print(c,end='')
    print('')
