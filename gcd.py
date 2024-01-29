def find_gcd(num1, num2):
    while num2:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1


if __name__ == "__main__":
    n1 = 18
    n2 = 12
    result = find_gcd(n1, n2)
    print(f"The GCD of {n1} and {n2} is: {result}")
