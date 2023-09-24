# https://py.checkio.org/en/mission/right-to-left/
"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""
def left_join(phrases: tuple[str]) -> str:
    # print("1",phrases)
    ph_list = list(phrases)
    ret_string = ""
    for i in range(0, len(phrases)):               
        if(i==len(phrases)-1):
            ret_string = ret_string + phrases[i] 
        else:
            ret_string = ret_string + phrases[i] +","         
        if(phrases[i].__contains__("right")):     
            # print(phrases[i])       
            ret_string = ret_string.replace("right", "left")    
            # print("# -",ret_string)        
            

    # print("Final -", ret_string)
    return ret_string


print("Example:")
print(left_join(("left", "right", "left", "stop")))

# # These "asserts" are used for self-checking
assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")