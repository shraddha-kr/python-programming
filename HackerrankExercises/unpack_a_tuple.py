fruits = ('Mango', 'Grapes', 'Banana')

green, red, blue = fruits

print(green, red, blue, sep=" ")

# Using Asterik
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)