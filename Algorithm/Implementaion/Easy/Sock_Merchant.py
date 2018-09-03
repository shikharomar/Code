#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    totalPair = 0
    check = [0]*len(ar)
    for index, val in enumerate(ar):
        if(check[index] == 0):
            sum = 1
            for i in range(index + 1, len(ar)):
                if(val == ar[i]):
                    check[i] = 1
                    sum +=1
            if(sum > 1):
                totalPair += sum // 2

    return totalPair



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
