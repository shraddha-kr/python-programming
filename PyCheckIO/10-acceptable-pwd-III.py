# https://py.checkio.org/en/mission/acceptable-password-iii/
def is_acceptable_password(password: str) -> bool:
   if((len(password)>6) and (any(chr.isdigit() for chr in password)) and (password.isdigit()==False)):
       return True
   else:
       return False


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False