import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    for j in range(n-1, -1, -1):
        print(arr[j], '', end='')
