x = 42
print(id(x))

# Confirm whether two variables are referencing the same object
y = x
print(id(x), id(y))

y = 78
print(id(x), id(y))
