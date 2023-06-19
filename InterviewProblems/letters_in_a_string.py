# SIEMENS
"""
Print the number of occurrences of a letter in a string
"""
user_input = input("Enter a string: ")
print(user_input)

letter_dict = {}
for i in user_input:
    if i in letter_dict:
        letter_dict[i] += letter_dict[i]
    else:
        letter_dict[i] = 1

# print(letter_dict)

# Using the collections module
from collections import Counter
test_str = "GeeksforGeeks"

res = Counter(test_str)

print(str(res))