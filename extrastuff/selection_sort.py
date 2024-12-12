# # sorting from minimum-->maximum



# # array: int = [22,3,45,6,234,23,1,2312,4,345,346,456,3,42,34]

# # # iterate through each element
# # for i in range(array):
# #     minimum_value = i

# # function to swap the element
# # def swap(i, j):
# #     swap_element = array[i]
# #     array[i] = array[j]
# #     array[j] =swap_element

# #     return array

# # def calculate_min(i, j):
# #     if array[i]<array[j]:
# #         return swap(i, j)
# #     return array

# # for i in range(0, len(array)):
# #     print(i)

# # # Iterate through the entire array to find the smallest element in the unsorted portion,
# # # for i in array:
# # #     print(i)

# # for i in range(len(array)):
# #     # print(f"Print 1 \n {i}") #--> prints the index
# #     # print(f"Print 2 \n {array[i]}") #--> prints the array
# #     pass

# # then swap it with the element at the current index. Repeat this process for each index

# # until the array is fully sorted.


def selection_sort(array):
    # length of an array
    n = len(array)
    # i = indexing (for index in range of length of an array - 1)
    for i in range(n-1):
        # assuming the i at beginning is max...
        max = i
        for j in range(i+1, n):
            if array[j] > array[max]:
                max = j
        array[i], array[max] = array[max], array[i]
        print(array)

# def selectionsort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         mini = i 
#         for j in range(i+1,n):                              #<<---
#             if arr[j]<arr[mini]:                              #     }
#                 mini = j                                         #     }
#         arr[i],arr[mini]=arr[mini],arr[i]           #<<---

# def selection_sort(array):
#     n = len(array)
#     for i in range(n-1):
#         mini = i
#         for j in range(i+1, n):
#             if array[j] < array[mini]:
#                 mini = j
#                 array[i], array[mini] = array[mini], array[i]
#                 print("sorting from mini",array)

# array = [2, 4, 1, 3, 5]
# selection_sort(array=array)

selection_sort(array=[2,5,4,3,1])