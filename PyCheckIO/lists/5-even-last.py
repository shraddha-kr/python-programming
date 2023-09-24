# https://py.checkio.org/en/mission/even-last/
"""
Slicing basics
mylist = [1,2,3,4,5,6,7,8,9,10]
for i in mylist[::2]:
    print i,
# prints 1 3 5 7 9

for i in mylist[1::2]:
    print i,
# prints 2 4 6 8 10
"""
def checkio(array: list[int]) -> int:
    sum = 0
    product = 0

    if(len(array)<1):
        return 0
    else:
        for i in range(0,len(array),2):
                print(i)
                sum = sum + array[i]            
            

        print("sum - ", sum)
        product =  sum * array[-1]
        print("product - ", product)
        return product
        


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# # These "asserts" are used for self-checking
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")