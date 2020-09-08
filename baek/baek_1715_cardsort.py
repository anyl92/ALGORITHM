import sys
sys.stdin = open('1715.txt', 'r')

import heapq
N = int(input())
L = [int(input()) for _ in range(N)]
heapq.heapify(L)

res = 0
while len(L) > 1:
    tmp1 = heapq.heappop(L)
    tmp2 = heapq.heappop(L)
    tmp = tmp1 + tmp2
    heapq.heappush(L, tmp)
    res += tmp
print(res)