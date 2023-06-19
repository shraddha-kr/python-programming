def hi(obj):
    print("Hi, I am", obj.name, "!")

class Robot:
    # pass
    # Binding the function "hi", to a class attribute "say_hi"
    say_hi = hi

x = Robot()
x.name = "Marvin"
hi(x)
Robot.say_hi(x)





















