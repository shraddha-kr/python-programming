arr = [4, 2, 2, 8, 3, 3, 1]

c_arr = [0]* 100
size = len(arr)

for i in range(0, size):
    print(arr[i])
    print(i)
    print(c_arr[arr[i]])
    print("--------------------")