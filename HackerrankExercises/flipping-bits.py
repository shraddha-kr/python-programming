#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here 
    res = "{:032b}".format(n)


    res_list = list(res)
    # print(*res_list)
    new_list = []
    for i in range(len(res_list)):
        if(res_list[i]=="0"):
            new_list.insert(i, "1")
        elif(res_list[i]=="1"):
            new_list.insert(i, "0")

    # print(*new_list)
    reverse = ""
    reverse = reverse.join(new_list)

    reverse = int(reverse, 2)
    # print(reverse)
    return reverse
                  
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
