# Python code to demonstrate working of in and is
# using "in" to check


if 's' in 'geeksforgeeks':
    print("s is part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")

# using "in" to loop through
for i in 'geeksforgeeks':
    print(i, end=" ")

# Is a carriage return
print("\r")

# using is to check object identity
# string is immutable( cannot be changed once allotted)
# hence occupy same memory location
print(' ' is ' ')

# using is to check object identity
# dictionary is mutable( can be changed once allotted)
# hence occupy different memory location
print({} is {})
