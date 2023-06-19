'''
5. Write a program that generates 50 random numbers such that the first number is between 1
and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
1 and 51.
'''

from random import randint

j = 2
for i in range(0, 50):   
    print('1 ', 'and ', j)
    print('Rnum - ', randint(1, j))
    j += 1
    print()
