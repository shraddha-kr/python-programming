import re
s1 = "Mayer is a very common Name"
s2 = "He is called Meyer but he isn't German."
print(re.search(r"M[ae][iy]er", s1))
print(re.search(r"M[ae][iy]er", s2))
 # matches because it starts with Mayer
print(re.match(r"M[ae][iy]er", s1)) 
# doesn't match because it doesn't start with Meyer or Meyer, Meier and so on:
print(re.match(r"M[ae][iy]er", s2))  