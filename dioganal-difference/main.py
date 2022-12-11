#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
#
# please run your code in hackerrank web site (https://www.hackerrank.com/challenges/diagonal-difference)
#
def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for value in range(len(arr)):
        sum1 += arr[value][value]
    a = len(arr[1])
    for value in range(len(arr)):
        sum2 += arr[value][a-1]
        a -= 1
    
    result = sum1 - sum2
    return abs(result)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)


    fptr.write(str(result) + '\n')

    fptr.close()
