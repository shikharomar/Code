#!/bin/python3
import math
import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if(n%2 == 0):
        n = n + 1
    fromBack = n - p
    turnFront = math.floor(p/2)
    turnBack = math.floor(fromBack/2)

    if(turnBack == turnFront):
        return turnBack
    else:
        return turnBack if turnBack < turnFront else turnFront

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
