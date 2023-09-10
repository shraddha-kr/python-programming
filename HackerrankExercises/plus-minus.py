# print("{:.6f}".format(2/5))
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
    pos = []
    neg = []
    zer = []   
    for n in arr:
        if(n==0):
            zer.append(n)
        elif(n<0):
            neg.append(n)
        else:
            pos.append(n)
    # print("pos - ", pos, "neg - ", neg, "zero - ", zer)    
    # Positive
    print("{:.6f}".format(len(pos)/len(arr)))
    # Negative
    print("{:.6f}".format(len(neg)/len(arr)))
    # Zero
    print("{:.6f}".format(len(zer)/len(arr)))

if __name__ == '__main__':
    # print("Please enter an input")
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    # print(arr)
    plusMinus(arr)