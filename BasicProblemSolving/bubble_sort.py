'''Bubble Sort :: Bubble sort is a simple sorting algorithm that exchanges adjacent elements in a list until the list is sorted. '''
# soln using built-in method
# user_list = [2, 6, 3, 1, 8, 4]
# sorted_list = sorted(user_list)
# print("list after sorting: ", sorted_list)

# def bubbleSort(array):
#     for i in range(len(array)):
#         # keep track of swapping, if array already sorted
#         swapped = False
#         for j in range(0, len(array)-i-1):
#             print("[i]: ", i, "[len(array)-i-1]: ", len(array)-i-1)
#             print("[j]: ",j, "[j+1]: ", j+1)
# # take user input
# list_a = input("Enter a list of numbers, separated by commas: ")
# a_list = [int(num) for num in list_a.split(',')]
#
# # print the list
# print("original list: ",a_list)
# print("lis after sorting: ",bubbleSort(a_list))

def bubble_sort(array):
    swapped = False
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
