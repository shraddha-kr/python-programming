'''
Populate a dictionary for a phone directory
'''

phone_dir = {}

terms = int(input("Please enter the total no of records in the directory you wish to add: "))
print(terms)

# Sol-1 by simple for loop
# for i in range(terms):
#      # populate the dict object with entries from user input
#      name = str(input())
#      phone_no = int(input())
#      phone_dir[name] = phone_no   #=> dict_items([('Shraddha', [963]), ('Shil', [852]), ('Rishi', [741])])

# Sol-2 by zip
names = []
phone_nos = []
for i in range(terms):
    names.append(str(input()))
    phone_nos.append(int(input()))


phone_dir = dict(zip(names, phone_nos)) #=> dict_items([('Shraddha', 369), ('Shil', 258), ('Rishi', 147)])

print(phone_dir.items())

# Sol-3 by fromkeys => TypeError: fromkeys expected at most 2 arguments, got 4

# d_keys = ['name', 'age', 'phone']
# name = ['shad', 'rishi', 'rohan', 'jyoti']
# age = [40, 8, 45, 70]
# phone = [963, 852, 741, 123]
# phone_dir = dict.fromkeys(d_keys, name, age, phone)
# check if duplicate key is allowed? => no it's not allowed, no excep is thrown, just one value out of the multiple is picked
print(phone_dir)
