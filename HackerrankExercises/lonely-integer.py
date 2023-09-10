#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    
    # initialize a null list
    
 
    # traverse for all elements
    for x in a:
        c = a.count(x)
        if(c==1):
            return x

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
