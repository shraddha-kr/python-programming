# all the items belonging to a Python list can be of different data type
# A Python list contains items separated by commas and enclosed within square brackets ([]).
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 1st till 2nd 
print (list[2:])        # Prints elements starting from 2nd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists