"""
if A=1, B=2, C=3 canonical total will be 6;
if D=4, E=5, F=6 canonical total will be 15;
if G=7, H=8, I=9 canonical total will be 24;

var input = "efg,ghi,abc";

var ouput = "abc,efg,ghi";
"""

userinput = input("Enter a string: ")
print(userinput)
userinput = userinput.split(",")
print(type(userinput))
userinput.sort()

for word in userinput:
    print(word)