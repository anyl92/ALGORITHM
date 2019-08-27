import sys
sys.stdin = open('input.txt', 'r')
L = [int(input()) for _ in range(9)]

n = len(L)
tmp = []
result = 0
res = []
for i in range(1<<n):
    for j in range(n+1):
        if i & (1<<j):
            tmp.append(L[j])

    if len(tmp) == 7:
        for i in tmp:
            result += i
        if result == 100:
            res = tmp
        result = 0
    tmp = []

for i in range(len(res)):
    for j in range(1+i, len(res)):
        if res[i] > res[j]:
            res[i], res[j] = res[j], res[i]
    print(res[i])