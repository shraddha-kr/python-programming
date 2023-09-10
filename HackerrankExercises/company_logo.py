#!/bin/python3
"""
Sample Input 0
aabbbccde


Sample Output 0

b 3
a 2
c 2
"""
import math
import os
import random
import re
import sys
from collections import Counter
from operator import itemgetter


if __name__ == '__main__':
    s = input()
    # ignore case
    s = s.lower()
    print(s)

    
    # sort aplhabetically
    sorted_s = ''.join(sorted(s))
    print(sorted_s)
    res = Counter(sorted_s)
    res_dict = dict(res)
    print("res_dict - ", res_dict)
    
    # sort on greatest occurence of a letter, i.e. by value of dict    
    # use itemgetter(0) for sorting using key
    sort_dict= dict(sorted(res_dict.items(), key=itemgetter(1), reverse=True)) 
    print("sort_dict - ", sort_dict)

    for x in list(sort_dict)[0:3]:
        print("{} {}".format(x,  sort_dict[x]))


