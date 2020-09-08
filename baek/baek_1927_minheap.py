import sys
sys.stdin = open('1927.txt', 'r')

import heapq
heap = []

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
