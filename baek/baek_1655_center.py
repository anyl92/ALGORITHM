import sys
import heapq
sys.stdin = open('1655.txt', 'r')

max_heap, min_heap = [], []
N = int(sys.stdin.readline())
for i in range(N):
    x = int(sys.stdin.readline())

    if i == 0:
        heapq.heappush(max_heap, x * -1)

    elif i == 1:
        if x >= max_heap[0] * -1:
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(min_heap, heapq.heappop(max_heap) * -1)
            heapq.heappush(max_heap, x * -1)

    else:
        if max_heap:
            left = max_heap[0] * -1
        if min_heap:
            right = min_heap[0]

        if x > left:
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(max_heap, x * -1)

    left_len = len(max_heap)
    right_len = len(min_heap)
    if left_len == right_len or left_len == right_len + 1:
        pass
    elif left_len > right_len:
        heapq.heappush(min_heap, heapq.heappop(max_heap) * -1)
    else:
        heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)

    if max_heap:
        print(max_heap[0] * -1)
    else:
        print(min_heap[0])
