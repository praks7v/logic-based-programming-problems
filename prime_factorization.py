def prime_factorization(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


numbers = int(input("Enter the number: "))
result = prime_factorization(numbers)
print(f"prime factorization of {numbers} : {result}")
