def f(n):
    return n + 42
def f(n,m=None):
    return n + m + 42

print(f(3, 4))
print(f(3))

# Either give a default or check for None to make it work

def f(n, m=None):
    if m:
        return n + m +42
    else:
        return n + 42
print(f(3), f(1, 3))
