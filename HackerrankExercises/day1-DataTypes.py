# Take user input without a asking prompt
i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
numUserInt = 0
numUserFloat = 0.0
strUserInput = ''

# Read and save an integer, double, and String to your variables.
numUserInt = int(input())
numUserFloat = float(input())
strUserInput = str(input())

# Print the sum of both integer variables on a new line.
print(i + numUserInt)

# Print the sum of the double variables on a new line.
print(round(d + numUserFloat, 1))

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s, strUserInput, sep='')





'''
i = 4
d = 4.0
s = 'HackerRank '

numUserInt = int(input("Enter an Integer Value: "))
numUserFloat = float(input("Enter a Float Value: "))
strUserInput = str(input("Enter a String Value: "))

print(type(numUserInt))
print(type(numUserFloat))
print(type(strUserInput))

# Print sum of 2 integers
if(isinstance(numUserInt, int)):   
   print(i + numUserInt)
else:
   print("User input is not a integer")

# Print sum of two floats
if(isinstance(numUserFloat, float)):
   print(round(d + numUserFloat, 1))
else:
   print("User input is not a float")

# Concat two strings
if(isinstance(strUserInput, str)):
   print(s, strUserInput, sep='')
else:
   print("User Input is not a string")

'''
