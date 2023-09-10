#!/bin/python3
"""
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

This is Matrix#  %!
"""
import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

row = int(first_multiple_input[0]) 

col = int(first_multiple_input[1])

# allow only alpha-numeric 
pattern = "[a-zA-Z0-9]+$."
# allow only special characters
special_pattern = "[^0-9a-zA-Z\s]+"
                   
matrix = []

for _ in range(row):
    matrix_item = input()
    # matrix_item = re.sub(special_pattern, ' ' ,matrix_item)
    matrix_item = re.sub("(?<=\w)\W+(?=\w)"," ",matrix_item)
    matrix.append(matrix_item)

print(matrix)
for i in range(0 , col):
    for j in range(0 , row):
        print(matrix[j][i], end="")

#OR
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
smat = ''

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(m):
    for j in range(n):
        smat += matrix[j][i]
print(re.sub(r'\b(\W)+\b', ' ', smat))