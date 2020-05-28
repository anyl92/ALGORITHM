prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

answer = 1
for i in range(40, 20, -1):
    temp, j = i, 0
    while j < 12:
        if not (temp % prime[j]):
            temp //= prime[j]
            answer *= prime[j]
        else:
            j += 1

for i in range(20, 1, -1):
    temp, j = i, 0
    while j < 12:
        if not (temp % prime[j]):
            temp //= prime[j]
            answer //= prime[j]
        else:
            j += 1

print(answer)