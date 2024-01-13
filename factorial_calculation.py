# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# number = int(input("Enter the non-negative integer: "))
# result = factorial(number)
# print(f"factorial of {number} is : {result}")


def factorial(n):
    results = 1
    for i in range(1, n + 1):
        results *= i
    return results


number = int(input("Enter the non-negative integer: "))
result = factorial(number)
print(f"factorial of {number} is : {result}")
