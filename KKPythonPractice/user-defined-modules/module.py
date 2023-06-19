# Called in main1.py
"""module.py - an example of a Python module"""

__counter = 0

def get_sum(list):
    global __counter
    sum = 0
    for element in list:
        __counter += 1
        sum += element
    return sum

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")    
    nums = [i+1 for i in range(5)]
    print(get_sum(nums) == 15)