def calculate_user_input():
    try:
        x = int(input("Enter a number: "))
        y = 1/x
        print(y)
    except:
        print("Something else went wrong")
        raise

    return None

calculate_user_input()