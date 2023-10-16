# https://py.checkio.org/en/mission/count-vowels/
def count_vowels(text: str) -> int:
    insen_str = list(text.casefold())
    vow_list = ['a', 'e', 'i', 'o', 'u']
    vow_count = 0
    for l in insen_str:       
        if(l in vow_list):
            vow_count = vow_count + 1            
    # your code here
    return vow_count


print("Example:")
print(count_vowels("Hello"))

# These "asserts" are used for self-checking
assert count_vowels("hello") == 2
assert count_vowels("openai") == 4
assert count_vowels("typescript") == 2
assert count_vowels("a") == 1
assert count_vowels("b") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
