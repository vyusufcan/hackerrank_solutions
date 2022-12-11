#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
#
# Please run it in Hackerrank web site ( https://www.hackerrank.com/challenges/compare-the-triplets )
#

def compareTriplets(a, b):
    playera_score = 0
    playerb_score = 0
    
    for value in range(3):
        if a[value] > b[value]:
            playera_score += 1
        elif b[value] > a[value]:
            playerb_score += 1
    
    return [playera_score,playerb_score]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
