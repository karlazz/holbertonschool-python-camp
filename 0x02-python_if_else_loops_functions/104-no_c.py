#!/usr/bin/python3
def no_c(str):
  while str.lower().find('c') > -1:
    pos=str.lower().find('c')
    str = str[:pos] + str[pos+1:]
  return str 

