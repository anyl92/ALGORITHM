import math

isPrime = [True for _ in range(2000001)]

for i in range(2, int(math.sqrt(2000001))+1):
    j = i*i
    while j <= 2000000:
        if isPrime[j]:
            isPrime[j] = False
        j += i

answer = 0
for i in range(2, 2000000):
    if isPrime[i]:
        answer += i
print(answer)