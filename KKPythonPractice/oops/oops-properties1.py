# A variable that is created and added to the object on initialization is called an "instance variable"
# hasAttr built-in function specifies whether an instance contains a certain attribute
# One of the default attributes of a class, which comes along whenever we create a class, is the __dict__.
# my_obj.__dict__
# MyClass.__dict__
class ExampleClass:
    def __init__(self, val = 1) -> None:
        
        self._first = val
    
    def set_second(self, val):
        # Made the variable private by adding two underscores
        self.__second = val

#1
example_obj_1 = ExampleClass(1)
#2
example_obj_2 = ExampleClass(2)
example_obj_2.set_second(3)
#3
example_obj_3 = ExampleClass(4)
# Obj can beadded a property on the fly
example_obj_3.third = 5

print(example_obj_1.__dict__)
print(example_obj_2.__dict__)
print(example_obj_3.__dict__)
