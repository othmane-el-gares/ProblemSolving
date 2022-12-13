#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n=len(arr)
    r1,r2,r3=0,0,0
    for x in arr :
        if x>0:
            r1+=1
        elif x<0:
            r2+=1
        else:
            r3+=1
    print("{:.6f}".format(r1/n))
    print("{:.6f}".format(r2/n))
    print("{:.6f}".format(r3/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
