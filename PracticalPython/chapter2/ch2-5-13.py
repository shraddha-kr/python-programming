'''
Use a for loop to print an upside down triangle like the one below.
Allow the user to specify how high the triangle should be.
****
***
**
*

'''
howHighVal = int(input('Enter how high you want the triangle: '))
for i in range(howHighVal, 0, -1):
    print('*' * i)
