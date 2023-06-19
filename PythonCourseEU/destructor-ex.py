class Robot():
    def __init__(self, name) -> None:
        print(name, "has been created")
    
    def __del__(self):
        print(self.name, "says bye-bye!")

if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y

    # AttributeError: 'Robot' object has no attribute 'name'
