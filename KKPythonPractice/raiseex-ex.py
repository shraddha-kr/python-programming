def calculate_user_input():    
    raise ZeroDivisionError
try:
    calculate_user_input()
except ZeroDivisionError:
    print("You cannot divide by Zero.")
except:
    print("Something else went wrong")    
    