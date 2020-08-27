import sys
sys.stdin = open('10819.txt', 'r')

import itertools

N = int(input())
L = list(map(int, input().split()))
perm = list(itertools.permutations(L, N))

res = 0
for j in perm:
    thisSum = 0
    for i in range(N-1):
        thisSum += abs(j[i] - j[i+1])
    if res < thisSum:
        res = thisSum

print(res)