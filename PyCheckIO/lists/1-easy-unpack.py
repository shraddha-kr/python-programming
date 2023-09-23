# https://py.checkio.org/en/mission/easy-unpack/
# 'tuple' object does not support item assignment, either convert it to a list and use its methods to do assignment
"""
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
OR
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
"""

def easy_unpack(elements: tuple) -> tuple:
    three_el_tuple = ()
    three_el_tuple = (elements[0], elements[2], elements[len(elements)-2])

    return three_el_tuple


print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

# These "asserts" are used for self-checking
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

print("The mission is done! Click 'Check Solution' to earn rewards!")