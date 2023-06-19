"""
Python KeyWords True and False are used to represent boolean values
in python, and are same as 1 and 0.
None : This is a special constant used to denote a null value or a void.
Its important to remember, 0, any empty container(e.g empty list) do not compute to None.
"""

print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

# showing that None is not equal to 0
# prints False as its false.
print (None == 0)

# showing objective of None
# two None value equated to None
# here x and y both are null
# hence true
x = None
y = None
print (x == y)

# showing logical operation
# or (returns True)
print(True or False)

# showing logical operation
# and (returns False)
print(False and True)

# showing logical operation
# not (returns False)
print(not True)