from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv


print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

height = input("How tall are you? ")
weight = input("Hou much do you weigh? ")


# If no args are provided, then the following error is thrown
# ValueError: not enough values to unpack (expected 4, got 1)
