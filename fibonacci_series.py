# def fibonacci(n):
#     fibo_series = [0, 1]
#     while len(fibo_series) < n:
#         fibo_series.append(fibo_series[-1] + fibo_series[-2])
#     return fibo_series
#
#
# number = int(input("Enter the number of terms for the fibonacci series: "))
# result = fibonacci(number)
# print(f'The fibonacci series up to {number} terms is: {result}')


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


number = int(input("Enter the number of terms for the fibonacci series: "))
fibonacci_series = [fibonacci_recursive(i) for i in range(number)]
print(f"the fibonacci series up to {number} terms is: {fibonacci_series}")
