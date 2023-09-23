#https://py.checkio.org/en/mission/between-markers-simplified/
"""
The find() method is almost the same as the index() method, 
the only difference is that the index() method raises an exception
if the value is not found. 
"""
def between_markers(text: str, start: str, end: str) -> str:
    initial = text.find(start)
    final = text.find(end)
    sub_str = text[initial+1:final] # the start marker index we don't want to include
    return sub_str


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"