# Strings are immutable sequence of data
print(len("Hello World!"))
# Concate
print("I love" +" Python!")
# Repeat
print("ha" *4)
# Character;s code point
print(ord("L"))
# Codepoints corres. char
print(chr(76))

# Strings can be treated as Lists
message = "The flight to New Yourk leaves tomorrow"

# Index a string
print(message[0])
print(message[1])

print("New York" in message)

"""Strings doesnot support deletion::TypeError: 'str' object doesn't support item deletion"""
# del message[0]
"""AttributeError: 'str' object has no attribute 'append'"""
message.append("from JFK")

# Lowest code point value is returned in case of min & max when used with strings
print(max("aAbBcC"))
print(min("Hello There"))
# if the chr doesnot exists, it throws an error
print("Hello World".index('w'))
print("Hello World".count("o"))
print("Hello".list())

