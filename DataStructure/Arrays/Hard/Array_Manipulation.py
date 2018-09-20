#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    ## Naive Solution ##
    # zeros = [0] * n
    #
    # for query in queries:
    #     for i in range(query[0]-1, query[1]):
    #         zeros[i] += query[2]
    #
    # return max(zeros)

    zeros = [0] * n
    breaks = []
    additions = []
    for query in queries:
        breaks.extend([query[0]-1, query[1]-1])
        additions.append(query[2])

    breaks.sort()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
