def find_max_min(lst):
    if not lst:
        return None, None
    max_element = min_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
        elif element < min_element:
            min_element = element
    return max_element, min_element


if __name__ == "__main__":
    my_list = [3, 5, 6, 7, 4, 7, 8, 1]
    max_value, min_value = find_max_min(my_list)
    print(f"maximum value is: {max_value}")
    print(f"minimum value is : {min_value}")
