tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
tup1[0] = 100; #TypeError: 'tuple' object does not support item assignment

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print(tup3)