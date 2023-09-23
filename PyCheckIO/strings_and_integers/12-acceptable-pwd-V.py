# https://py.checkio.org/en/mission/acceptable-password-v/

def is_acceptable_password(password: str) -> bool:
   if("password".lower()  in password.lower()):
       return False
   elif(len(password)>9):
       return True
   elif((len(password)>6 and len(password)<=9)):
        if(password.isdigit()==True):
            return False
        else:
            if((any(chr.isdigit() for chr in password))):
                return True
   else:
       return False


print("Example:")
print(len("1234567"))
print(is_acceptable_password("1234567"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True