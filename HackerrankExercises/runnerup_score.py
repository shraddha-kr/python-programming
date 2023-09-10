if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # remove duplicates
    arr = list(dict.fromkeys(arr))
    # sort the list
    arr = sorted(arr)
    print(arr)
    
    print(arr[-2])
 