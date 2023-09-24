# If you do not specify the index, the pop() method removes the last item.
# The del keyword also removes the specified index: del thislist[0]
# The remove() method removes the specified item. 

from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    if(len(items)<=1):
        return items
    else:
        # save the first el, that we want to shift to the last
        temp = items[0]
        # del the first el from the list
        items.pop(0)
        # move the first to the last
        items.append(temp)
        return items



# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
