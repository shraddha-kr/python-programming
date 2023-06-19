# Split
str_1 = "Hire the top 1% freelance developers"
list_1 = str_1.split()
print(list_1)

# Split with delimiter
str_1 = "Hire-the-top-1%-freelance-developers"

list_1 = str_1.split("-")
print(list_1)

# List method
str_1 = "Hire freelance developers"


list_1 = list(str_1.strip(" "))
print(list_1)
