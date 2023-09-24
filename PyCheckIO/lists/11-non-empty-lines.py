# https://py.checkio.org/en/mission/non-empty-lines/
def non_empty_lines(text: str) -> int:
    text = text.strip()
    # print(text)
    count = 0

    if(len(text))>0:
        str_list = text.split('\n')
        print(str_list)
               
        for i in range(len(str_list)):
            temp = str_list[i]
            
            if not (temp.isspace() or len(temp)==0):
                count = count + 1
                # print("cou - ",count) 

        # print("count - ",count)         
        return count
    else: # the text string is empty or it's length is 0
        return 0


print("Example:")
print(non_empty_lines("one simple line\n"))

# These "asserts" are used for self-checking
assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert (
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    )
    == 3
)
assert non_empty_lines('\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\nNullam ante ligula,\n          \n          fermentum a porta\n            ') == 5
print("The mission is done! Click 'Check Solution' to earn rewards!")