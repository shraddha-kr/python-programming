# 0,1,1,2,3,5,8,13 ...
nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if(nterms<=0):
    print("Enter a +ve no")
elif(nterms==1):
    print(n1)
else:
    while(count < nterms):
        print(n1)
        nth = n1 + n2
        # swap
        n1 = n2
        n2 = nth
        count += 1
        