#!/usr/bin/python3
def print_diagonal(n):
  if (n<1) :
    print('')
    return
  for i in range(0,n):
    print(i*' '+"\\")
