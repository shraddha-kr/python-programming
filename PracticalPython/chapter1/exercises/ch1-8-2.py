"""
Print a box like the one below.
*******************
* *
* *
*******************
"""
print("")
for x in range(4):
    if(x==1 or x==2):
        print("* *")
    else:
        print("*******************")
print("")
