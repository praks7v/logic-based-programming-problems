def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def find_lcm(num1, num2):
    gcd = find_gcd(num1, num2)
    lcm = (num1 * num2) // gcd
    return lcm


if __name__ == "__main__":
    n1 = 12
    n2 = 18

    result_lcm = find_lcm(n1, n2)
    print(f"The LCM of {n1} and {n2} is: {result_lcm}")
