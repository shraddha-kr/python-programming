'''
Print unique chars in a string
'''
from collections import Counter

input_string = "This is a unique string!"
print("input_string: ", input_string)

# split the words in the string with space as a separator
split_words = list(set(input_string.split()))
print("split_wrds: ", split_words)

# print unique chars in a a string
unique_chars = set(input_string)
no_of_unique = len(unique_chars)

print("unique_chars: ", unique_chars)
print("No of unique chars: ",no_of_unique)

# print the no of occurances of every char in a string
char_count = Counter(input_string.casefold()) # to count ignoring case
print(type(char_count))
print(char_count)
