#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    nmod3 = n%3
    if(nmod3==0):
        print('5'*n)
    elif(n/3>=1 and nmod3==2 and n>5):
        var = int((nmod3)/2)*5
        print('5'*(n-var)+'3'*(var))
    elif(n/3>=1 and nmod3==1 and n>10):
        var = int((nmod3)/1)*10
        print('5'*(n-var)+'3'*(var))
    elif(n%5==0):
        print('3'*n)
    else:
        print(-1)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)