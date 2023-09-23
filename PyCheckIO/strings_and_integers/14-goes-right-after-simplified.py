# https://py.checkio.org/en/mission/goes-right-after-simplified/
def goes_after(word: str, first: str, second: str) -> bool:
    # indx_first = -1
    # indx_second = -1
    # print(indx_first, indx_second)

    if(word.__contains__(first) and word.__contains__(second) and len(word)>1):
       indx_first = word.index(first)
       indx_second = word.index(second)
       if(indx_second == indx_first + 1):        
            return True 
    if((word.find(first)) or (word.find(second))):        
        return False
    elif(first==second):        
        return False
    else:      
        return False


print("Example:")
# print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")