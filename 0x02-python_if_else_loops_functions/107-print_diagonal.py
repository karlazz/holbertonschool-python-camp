#!/usr/bin/python3
def print_diagonal(n):
  if (n<1) :
    print('\n')
    return
  for i in range(0,n+1):
    print(i*' '+"\\")
