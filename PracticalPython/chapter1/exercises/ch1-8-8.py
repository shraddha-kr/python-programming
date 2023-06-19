"""
Write a program that asks the user to enter three numbers
(use three separate input statements).
Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average.
"""
num1 = eval(input('Enter number 1: '))
num2 = eval(input('Enter number 2: '))
num3 = eval(input('Enter number 3: '))
total = num1 + num2 + num3
average = (num1 + num2 + num3)/3
print("Total: ", total, "Average: ", average)
