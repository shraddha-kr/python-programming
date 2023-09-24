# https://py.checkio.org/en/mission/backward-each-word/
def backward_string_by_word(text: str) -> str:
    if(len(text)>0):
        w = text.split(" ")        
        nw = [i[::-1] for i in w]        
        # convert list to a string
        nw = " ".join(nw)
        
        return nw
    else:
        return ""

print("Example:")
print(backward_string_by_word(""))

# These "asserts" are used for self-checking
# assert backward_string_by_word("") == ""
# assert backward_string_by_word("world") == "dlrow"
# assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
# assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")