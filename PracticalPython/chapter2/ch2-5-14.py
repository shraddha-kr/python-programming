''''
Use for loops to print a diamond like the one below. Allow the user to
specify how high the diamond should be.
*
***
*****
*******
*****
***
*
'''
uInput = int(input("Enter a size for the diamond: "))
j = 2

for i in range(1, uInput):
    print(" " * (uInput-i), "* " * i)
    
for i in range(uInput, 1, -1):    
    print(" " * j, "* " * (uInput-j))
    j = j+1
    
