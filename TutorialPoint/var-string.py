 #Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:7])     # Prints characters starting from 2rd to 6th
print (str[2:])      # Prints string starting from 2rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string