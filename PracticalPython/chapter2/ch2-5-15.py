'''
Write a program that prints a giant letter A like the one below. Allow the user to specify how
large the letter should be.
     *
   *   *
   *****
 *       *
*         *
'''

userInput = int(input("Enter size of A: "))
mid = int(userInput/2)
j = 1

print("mid ", mid)
for i in range(1, (userInput+1)):
    if(i < mid):
       print(" " * (userInput-i), "* " * i)
    elif(i > mid):
        print(" " * (userInput-i), "* ", " " * j, " *")
        j = j + 2
    elif(i == mid):
        print(" " * (userInput-i), "*" * (i+2))
    
   
