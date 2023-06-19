"""
Binding attributes to objects is a general concept in Python. 
Even function names can be attributed. You can bind 
an attribute to a function name in the same way
"""
def f(x):
    return 42
f.x = 42
print(f.x)

"""
This can be used as a replacement for the static function variables of C and C++, 
which are not possible in Python
"""
def f(x):
    f.counter = getattr(f, "counter", 0) + 1
    return "Monty"
for i in range(10):
    f(i)
print(f.counter)