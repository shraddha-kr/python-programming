class Robot:
    pass

x = Robot()
y = Robot()
x.name = "Marvin"
x.build_year = "1979"
y.name = "Caliban"
y.build_year = "1993"
print(x.name)
print(y.build_year)

"""
The instances possess dictionaries __dict__, which they use to store their attributes and their corresponding values
"""
print(x.__dict__)
print(y.__dict__)

