class UnamedEx:
    try:
        x = int(input("Enter a number"))
        y = 1/x
        print(y)
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except:
        print("Smthing else went wrong")
print('All Done!')        
