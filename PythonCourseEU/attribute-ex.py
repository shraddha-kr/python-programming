class Robot(object):
    pass

x = Robot()
Robot.brand = "Kuka"
x.brand
x.brand = "Thales"
Robot.brand
y = Robot()
y.brand
Robot.brand = "Thales"
y.brand
x.__dict__

# Un-defined attribute, will give an Attribute Error
# x.energy 

# By using the function getattr, you can prevent this exception, 
# if you provide a default value as the third argument
getattr(x, 'energy', 100)