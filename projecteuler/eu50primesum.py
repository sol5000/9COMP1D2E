def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [2]
for i in range(3, 1000000, 2):
    if is_prime(i):
        primes.append(i)

max_length = 0
max_prime = 0
max_prime_list = []
for i in range(len(primes)):
    for j in range(i + max_length, len(primes)):
        s = sum(primes[i:j])
        if s >= 1000000:
            break
        if is_prime(s) and j - i > max_length:
            max_length = j - i
            max_prime = s
            max_prime_list = primes[i:j]

print(max_prime_list)
print(max_prime)
