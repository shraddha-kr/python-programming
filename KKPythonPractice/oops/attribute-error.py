# hasAttr specifies whether an instance contains a certain attribute
# When an obj's attribute that doesnot exist is accessed, python throws an Attribute Error

class Dog:
    def __init__(self, name) -> None:        
        self.name = name

dog = Dog("Max")
print(hasattr(dog, "name"))
print(dog.breed)