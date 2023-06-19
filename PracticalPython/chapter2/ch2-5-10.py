'''
Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be. [Hint: print('*'*10) prints ten asterisks.]
*******************
*******************
*******************
*******************
'''
howhigh = int(input("Enter how high the box you want: "))
symbol = input("Enter the symbol you want:- ")

for i in range(howhigh):
        print(symbol * howhigh)
