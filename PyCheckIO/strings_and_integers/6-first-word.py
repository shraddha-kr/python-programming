# https://py.checkio.org/en/mission/first-word-simplified/

def first_word(text: str) -> str:
    # partition returns a tuple by separating the string on the basis of the separator given
    print(text.partition(" ")[0])
    return text.partition(" ")[0]


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"