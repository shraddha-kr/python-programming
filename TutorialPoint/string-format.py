# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
str = "My name is {0} and weight is {1} kg!".format('Zara', 21)
str1 = "My name is %s and weight is %d kg!" % ('Zara', 21)
print(str1)