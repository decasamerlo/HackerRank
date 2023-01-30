#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    counter = [0,0,0]

    for value in arr:
        if value > 0:
            counter[0] += 1
        elif value < 0:
            counter[1] += 1
        else:
            counter[2] += 1
    
    print(round(counter[0]/len(arr), 6))
    print(round(counter[1]/len(arr), 6))
    print(round(counter[2]/len(arr), 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
