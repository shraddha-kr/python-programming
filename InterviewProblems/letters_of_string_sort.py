s ="GEEKSFORGEEKS"
 
li = []
l = len(s)
for i in range (0,l):
    li.append(s[i])
 
 
for i in range(0,l):
    for j in range(0,l):
        # print(li[i], li[j])
        if li[i]<li[j]:
            li[i],li[j]=li[j],li[i]
            print(li[i], li[j])

j=""
print(li)
for i in range(0,l):
    j = j+li[i]
 
print(j)  

       