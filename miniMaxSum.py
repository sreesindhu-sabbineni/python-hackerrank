#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    minsum = 0
    maxsum = 0
    for i in range(0,len(arr)-1):
        minsum += arr[i]
    for i in range(1, len(arr)):
        maxsum += arr[i]
    print('{} {}'.format(minsum,maxsum))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
