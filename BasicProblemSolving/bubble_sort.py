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

# skip sorting a sorted list
def bubble_sort(array):
    
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array)-i-1):
            if(array[j] > array[j+1]):
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
                swapped = True
        if not swapped:
            break
    
if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    bubble_sort(data)
    print(data)
