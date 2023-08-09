# % operator returns True if there is a remainder from 
# the expression, and returns False if there is no remainder 
def f(x):
    return x + 4

numbers = [3, 7, 2, 9, 12]

# Assign the result only when the there is remainder after adding 4
#  to every no from the list
odd_numbers = [result for x in numbers if (result:=f(x)) % 2]
print(odd_numbers)