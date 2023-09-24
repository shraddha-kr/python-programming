# https://py.checkio.org/en/mission/backward-each-word/
def backward_string_by_word(text: str) -> str:
    temp = ""
    if(len(text)>0):
        # txt_list = text.split()
        # for i in range(len(txt_list)):
        #     temp = txt_list[i]
        #     txt_list[i] = temp[::-1]

        # print("reverse_list: ", txt_list)
        text = text[::-1]
        print(text)
        return text
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