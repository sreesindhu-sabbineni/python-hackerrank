#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(n):
    i = 1
    for j in reversed(range(0, n)):
        print(' ' * (j) + '#' * i)
        i += 1


if __name__ == '__main__':
    n = int(input())

    staircase(n)
