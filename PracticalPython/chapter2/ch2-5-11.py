'''
Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be.
*******************
*                 *
*                 *
*******************
'''

howHigh = int(input('Enter how high you want the box: '))

for i in range(howHigh):
    if(i==0 or i==howHigh-1):
        print('*' * howHigh)
    else:        
        print('*', ' '*(howHigh-4), '*')
