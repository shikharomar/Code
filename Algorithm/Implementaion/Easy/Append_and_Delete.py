#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    initial = len(s)
    final = len(t)

    if initial == final and final == 0: # For Null strings
        return "Yes"

    if initial > final:
        longer = initial
        shorter = final
    else:
        longer = final
        shorter = initial

    for i in range(shorter): # Finding the common string
        if s[i] != t[i]:
            break
        if i == shorter - 1:
            i += 1


    if initial + final <= k: # Case I: If k is large enough
        return "Yes"

    initial -= i             # Subtracting common string length from original strings'
    final -= i


    if (initial + final)%2 == k%2: # Checking k with (initial + final), if both are simultaneously even or odd
        if initial + final <= k:   # Checking if k is large enough for the operation
            return "Yes"
        else:
            return "No"
    else:
        return "No"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
