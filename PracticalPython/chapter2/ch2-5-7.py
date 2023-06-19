'''
Write a program that uses exactly four for loops to print the sequence of letters below.
AAAAAAAAAABCDBCDBCDBCDBCDEFFFFFFFFFFFFFFF
'''
for i in range(10):
    print('A', end='')
for i in range(5):
    print('BCD', end='')
print('E', end='')
for i in range(15):
    print('F', end='')
print()
