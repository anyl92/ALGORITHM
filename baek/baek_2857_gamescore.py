import sys
sys.stdin = open('2847.txt', 'r')

N = int(input())
L = [int(input()) for _ in range(N)]

res = 0
for i in range(len(L) - 1, 0, -1):
    if L[i] <= L[i - 1]:
        res += L[i - 1] - (L[i] - 1)
        L[i-1] = L[i] - 1
print(res)