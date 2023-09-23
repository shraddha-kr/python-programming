# https://py.checkio.org/en/mission/backward-string/

def backward_string(valstring: str) -> str:
    print(valstring[::-1])
    return valstring[::-1]



assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"