"""
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
"""
r = 4
c = 2
arr1 =  [['Tsi'],
        ['h x'],
        ['i  '],
        ['sM '],
        [' a ']]
m = 3
n = 2
arr =  [[1, 2],
           [4, 5],
           [7, 8]]
# # Row-wise traversal
# print("Row-wise traversal:", end = " ")
# for i in range(0 , m):
#     for j in range(0 , n):
#         print(arr[i][j],end=" ")

# Column-wise traversal
print("\nColumn-wise traversal:", end=" ")
for i in range(0 , n):
    for j in range(0 , m):
        print(arr[j][i], end=" ")