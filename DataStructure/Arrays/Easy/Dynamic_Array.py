#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    result = []
    seqList = []
    for i in range(n):
        seqList.append([])
    lastAnswer = 0
    for query in queries:
        if query[0] == 1:
            seqNum = (query[1] ^ lastAnswer) % n
            seqList[seqNum].append(query[2])
        else:
            seqNum = (query[1] ^ lastAnswer) % n
            elemIndex = query[2] % len(seqList[seqNum])
            lastAnswer = seqList[seqNum][elemIndex]
            result.append(lastAnswer)
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
