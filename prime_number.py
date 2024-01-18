def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 2:
            return False
    return True


if __name__ == "__main__":
    input_number = int(input("Enter the number: "))
    if is_prime(input_number):
        print(f"{input_number} is prime number")
    else:
        print(f"{input_number} isn't a prime number.")
