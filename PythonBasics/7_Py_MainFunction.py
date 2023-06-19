"""
Python program to illustrate function with main
"""


def get_integer():
    result = int(input("Enter Integer: "))
    return result


def main():
    print("Started")

    print("This is my file to test Python's execution methods.")
    print("The variable __name__ tells me which context this file is running in.")

    # It will print the representation of the __name__ variable
    # using Python's built-in repr()
    print("The value of __name__ is:", repr(__name__))

    # calling the getInteger function and
    # storing its returned value in the output variable
    output = get_integer()
    print(output)


# now we are required to tell Python
# for 'main' function existence

if __name__ == "__main__":
    main()
