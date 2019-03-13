#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minmax = [0,0]
    minscore = scores[0]
    maxscore = scores[0]
    for i in range(1,len(scores)):
        if scores[i]>maxscore:
            maxscore=scores[i]
            minmax[0] += 1
        if scores[i]<minscore:
            minscore=scores[i]
            minmax[1] += 1
    return minmax



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
