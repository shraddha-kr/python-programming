# https://py.checkio.org/en/mission/most-wanted-letter/
# Refer - https://note.nkmk.me/en/python-dict-get-key-from-value/

from collections import Counter

def checkio(text: str) -> str:
    # lower case
    lower_str = text.lower()
    # print(lower_str)

    # remove spaces & special chars
    lower_str = "".join(l for l in lower_str if l.isalnum())  
    # print(lower_str)

    # count the occurences
    res = Counter(lower_str)
    # print(res)

    # sort on dict value
    sorted_vallist = sorted(res.items(), key=lambda x:x[1]) # 0 is key, 1 is value
    
    # get the last item value from the sorted dict
    sorteddict = dict(sorted_vallist)    
    print(sorteddict)

    res_keylist = [k for k,v in sorteddict.items() if v == list(sorteddict.values())[-1]]
    print(res_keylist)

    # sort resultant list alphabetically
    res_keylist.sort()
    print(res_keylist)

    return res_keylist[0]


print("Example:")
# print(checkio("Hello World!"))

# These "asserts" are used for self-checking
# assert checkio("Hello World!") == "l"
# assert checkio("How do you do?") == "o"
# assert checkio("One") == "e"
# assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
# assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")