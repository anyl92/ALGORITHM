import sys
sys.stdin = open('11279.txt', 'r')

import heapq
heap = []

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap) * (-1))
        else:
            print(0)
    else:
        heapq.heappush(heap, x * (-1))
        # heapq.heappush(heap, (-x, x))