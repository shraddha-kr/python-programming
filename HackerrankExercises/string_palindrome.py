input_string = input("Enter a String: ")
if(input_string==input_string[::-1]):
    print("String is a palindrom!")
else:
    print("String is not a palindrom!")

# More efficient version
# Program to check if a string is palindrome or not

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")    