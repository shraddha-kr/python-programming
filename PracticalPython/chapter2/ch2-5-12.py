'''

Use a for loop to print a triangle like the one below. Allow the user to
specify how high the triangle should be.
*
**
***
****

'''
howHighVal = int(input('Enter how high you want triangle: '))
for i in range(1, howHighVal+1):
    print("*" * i)
