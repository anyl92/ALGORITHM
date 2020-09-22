import sys
sys.stdin = open('2812.txt', 'r')

N, K = map(int, input().split())
L = list(map(int, input()))

s = []
cnt = 0

for i in L:
    while s and cnt < K and s[-1] < i:
        s.pop()
        K -= 1
    s.append(i)

while cnt < K:
    s.pop()
    K -= 1

for res in s:
    print(res, end='')

# res = ''.join(L[K:])
# if N-K-1 == 0:
#     print(str(max(L)))
#
# for i in range(N-K-1):
#     res_list = L[i:i+N]
#     if int(res_list[0]) < int(res[0]):
#         continue
#     if len(res_list) < N-K:
#         continue
#
#     j = 1
#     while len(res_list) > N-K:
#         if len(res_list) == 2:
#             if res_list[0] < res_list[1]:
#                 res_list.pop(0)
#             else:
#                 res_list.pop()
#         elif res_list[j] < res_list[j+1]:
#             res_list.pop(j)
#         else:
#             res_list.pop(res_list.index(min(res_list)))
#             j -= 1
#         j += 1
#
#     tmp = ''.join(res_list)
#     if int(res) < int(tmp):
#         res = tmp
# print(res)
