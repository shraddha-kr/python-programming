'''3. Write a program that generates a random number between 1 and 10 and prints your name
that many times.
'''
from random import randint

num = randint(1, 10)
print('num -', num)

for i in range(0, num):
    print('Shraddha')
