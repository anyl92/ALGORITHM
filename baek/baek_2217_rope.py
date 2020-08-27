import sys
sys.stdin = open('rope_input.txt', 'r')

N = int(input())
L = [int(input()) for _ in range(N)]
L.sort()

maxx = 0
for i in range(N):
    res = L[i] * (N - i)
    if res > maxx:
        maxx = res
print(maxx)