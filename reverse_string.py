def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


if __name__ == "__main__":
    input_string = "Hello, World!"
    result = reverse_string(input_string)
    print(result)
