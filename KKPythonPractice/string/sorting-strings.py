# Returns a new sorted list from a list or string
print(sorted(["kiwi", "apple", "mango"]))
print(sorted("Sort Me!"))


# Modifies the list on which the method is invoked by sorting the elements
fruits = ["kiwi", "apple", "mango"]
sorted_fruits = fruits.sort()
print(fruits)