
# https://www.educative.io/answers/how-to-separate-even-and-odd-numbers-in-a-python-list 
# https://www.sanfoundry.com/python-program-even-odd-elements-different-lists/
# https://github.com/topics/python-problem-solving

even_odd_list = [2, 5, 78, 93, 3, 15, 34, 7, 8, 5, 1, 9]

even = []
odd = []
separated = []
two = []
three = []

for num in even_odd_list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

even.sort()
odd.sort()

separated.append(even)
separated.append(odd)

print("Appended - ", separated) 

two = even + odd
print("Added - ", two) 

even.extend(odd) # return type is 'None', so cannot be assigned to a new list
print("Extended - ", even) 