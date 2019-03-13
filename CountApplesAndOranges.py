#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applecount = 0
    orangecount = 0
    for i in range(0,len(apples)):
        if s<=(apples[i]+a)<=t:
            applecount+=1
    for i in range(0,len(oranges)):
        if s<=(oranges[i]+b)<=t:
            orangecount+=1
    print(applecount)
    print(orangecount)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
