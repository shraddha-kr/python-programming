# Slicing basics
# mylist = [1,2,3,4,5,6,7,8,9,10]
mylist = [1, 3, 5]
for i in mylist[::2]:
    print(i)
# prints 1 3 5 7 9

for i in mylist[1::2]:
    print(i)
# prints 2 4 6 8 10