def isPrime(n):
    i = 2
    while i <= n//2:
        if n % i == 0:
            return 2
        i += 1
    return 1

print(isPrime(4))