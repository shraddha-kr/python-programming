first_list = []
for x in range(5):
    first_list.append(10 ** x)
print(first_list)

second_list = [10 ** x for x in range(10)]
# print(second_list)

second_list = [1 if x % 2 == 0 else 0 for x in range(10)]
print(second_list)
