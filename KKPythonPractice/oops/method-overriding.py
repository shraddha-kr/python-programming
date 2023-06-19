# Method Overriding in single inheritance
class ClassA:
    number = 100

    def multiply(self, amount):
        print(self.number * amount)

class ClassB:
    number = 200

    def multiply(self, amount):
        print(self.number * amount)  

# In case of multiple inheritance the resolution happens for class from left to right
class ClassC(ClassB, ClassA):
    pass

my_instance = ClassC()

print(my_instance.number)
my_instance.multiply(2)

