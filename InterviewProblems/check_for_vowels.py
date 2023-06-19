"""
Given a string, the task is to check if every vowel is present or not. We consider a vowel to be present if it is present in upper case or lower case. i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ . 
Examples : 

Input : geeksforgeeks
Output : Not Accepted
All vowels except 'a','i','u' are not present

Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present
"""
# Using without built-in methods
def check(string):
    string = string.lower()
    vowels = set("aeiou")

    s = set()
    print(type(s))
    for char in string:
        if char in vowels:
            s.add(char)            
        else:
            pass

    if len(s) == len(vowels):
        print("Accepted")
    else:
        print("Not Accepted")

# Using Set Methods
# def checks(string):
#     if set("aeiou").issubset(set(string.lower())):
#         return "Accepted"
#     return "Not Accepted"

if __name__ == "__main__":
    string = "SEEquoial"

    print(check(string))