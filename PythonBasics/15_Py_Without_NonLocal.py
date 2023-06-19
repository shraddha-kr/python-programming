def outer():
    a = 5
    print('outer')

    def inner():
        print('inner')
        a = 10
        print(a)
        
    print('Calling inner ...')   
    inner()

    print(a)

print('Calling outer ...')
outer()
