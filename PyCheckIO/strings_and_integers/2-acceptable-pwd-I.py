# https://py.checkio.org/en/mission/acceptable-password-i/
def is_acceptable_password(password: str) -> bool:
    if(len(password)>6):
        return True
    else:
        return False


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False