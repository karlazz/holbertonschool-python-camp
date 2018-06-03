#!/usr/bin/python3
print("{}".format('01'), end='')
for i in range(0,10):
  for j in range(2,10):
    if(j>i):
      print(", {}{}".format(i,j),end='')
print("{}".format(''))
