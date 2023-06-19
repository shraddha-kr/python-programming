class A:
    Var = n = 1
    def __init__(self, val):
        self.val = value = 2

a = A(3)

print('n' in a.__dict__)

print('val' in A.__dict__)

print('Var' in A.__dict__)

print('value' in a.__dict__)

print(hasattr(a, 'n'))