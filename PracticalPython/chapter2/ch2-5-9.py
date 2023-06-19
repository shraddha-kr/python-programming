'''
The Fibonacci numbers are the sequence below, where the first two numbers are 1,
and each number thereafter is the sum of the two preceding numbers.
Write a program that asks the user how many Fibonacci numbers to print and then prints that many.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .
'''

prevNum = 0
currNum = 0
fibArr = []
#print(len(fibArr))

limit = int(input('How many Fibonacci numbers to print: '))
for i in range(limit):    

    if(i<=1):
       fibArr.append(1)
       print(1)
    else:
       currNum = fibArr[i-1]
       prevNum = fibArr[i-2]
       fibArr.append(currNum + prevNum)
       print(currNum + prevNum)

