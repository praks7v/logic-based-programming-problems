def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]


if __name__ == "__main__":
    input_string = input("Enter the string: ")
    if is_palindrome(input_string):
        print(f"'{input_string}' is a palindrome.")
    else:
        print(f"'{input_string}' is not a palindrome.")
