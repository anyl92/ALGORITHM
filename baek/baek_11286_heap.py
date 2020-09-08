import sys
import heapq
sys.stdin = open('11286.txt', 'r')
heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:  # 절댓값과 원래값 넣기
        if x > 0:
            heapq.heappush(heap, (x, x))
        else:
            heapq.heappush(heap, (-x, x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

# res = []
# for x in L:
#     if x != 0:
#         res.append([x, abs(x)])
#     else:
#         if res:
#             if len(res) > 1:
#                 res.sort(key=lambda y: (y[1], y[0]))
#             tmp, _ = res.pop(0)
#             print(tmp)
#         else:
#             print(0)
