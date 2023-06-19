"""
Print a triangle like the one below.
*
**
***
****
"""
print()
for i in range(4):
    for j in range(0, i+1):
        print("*", end="")
    print()
