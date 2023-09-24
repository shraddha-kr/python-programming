# https://py.checkio.org/en/mission/duplicate-zeros/
mylist = [1,2,0,4,0,6,0,8,0,10]
zero_idx = 0
idx_list = mylist.copy()
counter = 0

# find if 0 is present
for i in range(len(mylist)):
    if(mylist[i]==0):        
# find the index at which 0 is present
        zero_idx = i+1+counter
        print(zero_idx)
        # insert one more 0 at index+1 of the original zero
        idx_list.insert(zero_idx, 0)
        counter+=1

print(mylist)
print(idx_list)
