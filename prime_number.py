# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, number):
#         if number % i == 2:
#             return False
#     return True
#
#
# if __name__ == "__main__":
#     input_number = int(input("Enter the number: "))
#     if is_prime(input_number):
#         print(f"{input_number} is prime number")
#     else:
#         print(f"{input_number} isn't a prime number.")


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# Example usage:
user_input = int(input("Enter a number to check if it's prime: "))
if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")
