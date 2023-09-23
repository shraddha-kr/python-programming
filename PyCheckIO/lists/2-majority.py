#https://py.checkio.org/en/mission/majority/
def is_majority(items: list[bool]) -> bool:
    true_count = 0
    false_count = 0
    
    if(len(items)<1):
        return False
    else:
        for i in range(len(items)):
            if(items[i])==True:
                true_count += 1
            elif(items[i])==False:
                false_count+=1
            
    if(true_count == false_count):
        return False
    elif(false_count > true_count):
        return False
    elif(true_count > false_count):
        return True

    


print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False
