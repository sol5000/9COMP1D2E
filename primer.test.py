def is_prime(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

n = int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")