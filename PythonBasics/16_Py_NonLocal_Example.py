# demonstrating non local  
# inner loop changing the value of outer a 
# prints 10

print ("Value of using nonlocal is : ",end="")

def outer():
    print('outer')
    a = 5
    print(a)
    
    def inner(): 
        print('inner')
        nonlocal a  
        a = 10
        print(a)

    print('Calling inner...')    
    inner() 
    print (a) 

print('Calling outer...')
outer() 
