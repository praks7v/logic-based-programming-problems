def is_armstrong_strong(num):
    num_str = str(num)
    num_digits = len(num_str)

    armstrong_sum = 0
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits
    return armstrong_sum == num


if __name__ == "__main__":
    num_to_check = 153
    if is_armstrong_strong(num_to_check):
        print(f"{num_to_check} is an Armstrong number.")
    else:
        print(f"{num_to_check} is not an Armstrong number.")
