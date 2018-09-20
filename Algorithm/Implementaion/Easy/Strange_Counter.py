#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    def power2(num):
        i = -1
        while math.floor(num):
            num /= 2
            i += 1
        return math.pow(2, i)
    start_time = 3 * power2((t + 2)//3) - 2
    counter_shows = (start_time + 2) - (t - start_time)

    return int(counter_shows)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
