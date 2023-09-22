# 0, 1, 1, 2, 3, 5, 8....
terms = int(input())

n1, n2 = 0, 1, 
count = 0
nth = 0

# assuming terms is > 1
if(terms==1):
    print(n1)
else:
    for count in range(terms):        
        nth = n1 + n2
        print(n1)

        # swap
        n1 = n2
        n2 = nth
        count += 1