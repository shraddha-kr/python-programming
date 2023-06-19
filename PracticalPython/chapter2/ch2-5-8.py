'''
8. Write a program that asks the user for their name and how many times
to print it. The program
should print out the user’s name the specified number of times.
'''
name = input('Enter you name: ')
times = int(input('No of times you want it printed: '))
print()
for i in range(times):
    print(name)
