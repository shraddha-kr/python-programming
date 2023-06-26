#https://py.checkio.org/en/mission/between-markers-simplified/

def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    return ""


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"