n = 0
res = 0

while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        res += n
    n += 1

print(res)