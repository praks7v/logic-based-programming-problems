def count_digits(number):
    num_str = str(number)
    count_digit = len(num_str)
    return count_digit


if __name__ == "__main__":
    n = 123456
    result = count_digits(n)
    print(f"the number of in {n} is: {result}")
