class Dog:
    def __init__(self, name) -> None:
        self.name = name

    def bark(self):
        print("Woof")

pet1 = Dog("Max")
pet2 = Dog("Daisy")

# name of the class
print(Dog.__name__)
# name of the class the object bwlongs to
print(type(pet1).__name__)
# main is the module since directly the file is run
print(pet1.__module__)

class Chihuahua(Dog):
    def __init__(self, name) -> None:
        super().__init__(self, name)
        self.size = "small"

for base in Chihuahua.__bases__:
    print("Superclass name ", base)
