# Called in main.py
import module2

# print("I m in module - 1")

print(__name__)

if __name__ == "__main__":
    print("I am not in a module")