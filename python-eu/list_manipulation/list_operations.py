# PEEK: Which can be used to view what is on the top of the stack 
# without removing this element, A peek can be simulated by accessing 
# the element with the index -1
lst = ["easy", "simple", "cheap", "free"]
print(lst[-1])

# APPEND: Add an item to an existing list
lst.append("justice")
print(lst[-1])

# APPEND returns a 'None', when re-assignment to the existing list is done
lst = lst.append("respect")
print(lst)

# POP: Returns the "i"th element of a list. the element will be removed 
# from the list as well
# The POP raises an IndexError exception, if the list is empty or the index
# is out of range
cities = ["Hamburg", "Linz", "Salzburg", "Vienna"]
ret_city = cities.pop(0)
print(ret_city)
print(cities)

# The method 'pop' can be called without an argument. 
# In this case, the last element will be returned. 
# So s.pop() is equivalent to s.pop(-1).
last_city = cities.pop()
print(last_city)
print(cities)

# APPEND another sublist, you want to add all the elements of another 
# list to your list. 
# If you use append, the other list will be appended as a sublist.
lst = [42,98,77]
lst2 = [8,69]
lst.append(lst2)
print(lst)  # lst = [42,98,77, [8, 69]]

# EXTEND Python provides the method 'extend'. It extends a list by appending 
# all the elements of an iterable like a list, a tuple or a string to a list
# EXTEND A LIST
lst = [42,98,77]
lst2 = [8,69]
lst.extend(lst2)
print(lst) # lst = [42, 98, 77, 8, 69]

# IMP SEE THE BRACKETS, YOU ARE EXTENDING ANOTHER LIST
L = [3, 4]
L.extend([42])
print(L)

# EXTEND A STRING
lst = ["a", "b", "c"]
programming_language = "Python"
lst.extend(programming_language)
print(lst)

# EXTEND A TUPLE
lst = ["Java", "C", "PHP"]
t = ("C#", "Jython", "Python", "IronPython")
lst.extend(t)
lst

# "+" ALTERNATIVE There is an alternative to 'append' and 'extend'. '+' can be used to combine lists.
level = ["beginner", "intermediate", "advanced"]
other_words = ["novice", "expert"]
level + other_words

# REMOVE This call will remove the first occurrence of 'x' from the 
# list 's'. If 'x' is not in the list, a ValueError will be raised. 
# We will call the remove method three times in the following example
# to remove the colour "green". As the colour "green" occurrs only 
# twice in the list, we get a ValueError at the third time.
colours = ["red", "green", "blue", "green", "yellow"]
colours.remove("green")
colours

# INDEX It returns the first index of the value x. 
# A ValueError will be raised, if the value is not present. 
# If the optional parameter i is given, the search will start 
# at the index i. 
# If j is also given, the search will stop at position j.
colours = ["red", "green", "blue", "green", "yellow"]
colours.index("green")
colours.index("green", 3,4)

# "INSERT"  To work efficiently with a list, we need also a way to add elements to arbitrary positions inside of a list. 
# This can be done with the method "insert":An object "object" will be included in the list "s". "object" will be placed before the element s[index]. s[index] will be "object" and all the other elements will be moved one to the right.

lst = ["German is spoken", "in Germany,", "Austria", "Switzerland"]
lst.insert(3, "and")
lst
abc = ["a","b","c"]
abc.insert(len(abc),"d")
abc
