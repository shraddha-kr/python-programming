# https://py.checkio.org/en/mission/middle-characters/
def middle(text: str) -> str:
    # length
    len_str = len(text)      
    # start-index
    indx_start = -1
    print(len_str, indx_start, sep=" ")

    # even
    if(len_str % 2 == 0):
        indx_start = len_str//2
        print(indx_start)
        print(text[indx_start-1:indx_start+1])
        return text[indx_start-1:indx_start+1]
    # odd
    else:
        indx_start = len_str//2
        print(indx_start)
        return text[indx_start]


print("Example:")
# print(middle("example"))

# # These "asserts" are used for self-checking
# assert middle("example") == "m"
# assert middle("test") == "es"
assert middle('very-very long sentence') == 'o'
print("The mission is done! Click 'Check Solution' to earn rewards!")
