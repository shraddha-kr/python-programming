#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Since Python's int is essentially boundless there will never be an overflow issue.
    # https://stackoverflow.com/questions/41217302/how-can-i-initialize-and-use-64-bit-integer-in-python3   
    arr.sort()   
    min_sum = sum(arr[0:-1])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
