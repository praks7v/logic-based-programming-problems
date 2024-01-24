def linear_search(lst, target):
    for i, element in enumerate(lst):
        if element == target:
            return i
    return -1


# def linear_search_without_enumerate(lst, target):
#     for i in range(len(lst)):
#         if lst[i] == target:
#             return i
#     return -1


my_list = [3, 4, 1, 7, 8, 9, 6, 5, 2]
target_element = 21
index = linear_search(my_list, target_element)
if index != -1:
    print(f"The element {target_element} found at the element {index}")
else:
    print(f"The element {target_element} not found in the list.")
