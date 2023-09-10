import os


def diagonalDifference(arr, n):
    # Initialize sums of diagonals
    d1 = 0
    d2 = 0
 
    for i in range(0, n):
     
        for j in range(0, n):
         
            # finding sum of primary diagonal
            if (i == j):
                d1 += arr[i][j]
 
            # finding sum of secondary diagonal
            if (i == n - j - 1):
                d2 += arr[i][j]
         
    # Absolute difference of the sums
    # across the diagonals
    return abs(d1 - d2);
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
