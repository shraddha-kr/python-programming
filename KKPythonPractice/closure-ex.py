def outer_fun(x):
    def inner_fun(y):
        return x * y

    return inner_fun


var_one = outer_fun(4)
print(var_one(3))    