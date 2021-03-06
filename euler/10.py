import math

isPrime = [True for _ in range(2000001)]

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(2000001))+1):
    print(i)
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