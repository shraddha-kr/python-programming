"""
Write a program that uses a for loop to print the numbers
8, 11, 14, 17, 20, . . . , 83, 86, 89.
"""
for i in range(5, 87, 3):
    i = i + 3
    print(i, sep=", ")
