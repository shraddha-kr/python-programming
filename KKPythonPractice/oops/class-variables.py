"""Contrary to instance variables, class variables are stored outside any object, thus:

- they aren't shown in an object's __dict__

- they always return the same value in all class instances (objects), except if they are altered inside the class method. In the latter case, any new object that invokes that method, alters the class variable's value

- they can still be accessed with the hasattr() function and with object.<variable> notation

- they can be private like any other properties and accessed with '_ClassName__PrivatePropertyName' notation"""


class ObjCounter:
    __counter = 0

    def __init__(self, val=1):
        self.__first = val
        ObjCounter.__counter += 1


object_1 = ObjCounter()
object_2 = ObjCounter(2)
object_3 = ObjCounter(4)

print("Object_2 first: ", object_2._ObjCounter__first)
print("Object_3 first: ", object_3._ObjCounter__first)
print("We have created", end=" ")
print(object_3._ObjCounter__counter, "objects")
print("Counter inside the ObjCounter is now", end=" ")
print(ObjCounter.__dict__["_ObjCounter__counter"])