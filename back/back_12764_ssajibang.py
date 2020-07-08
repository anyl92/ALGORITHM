import sys
sys.stdin = open('12764.txt', 'r')

# TLE 10%
# from collections import deque
#
# N = int(input())
# L = [list(map(int, input().split())) for _ in range(N)]
#
# com_list = deque([0])
# cnt_list = deque([0])
#
# for l in L:
#     tmp = l[1] - l[0]
#     l[1] = tmp
# L.sort(key=lambda x:x[0])
#
# time, chk_idx = 0, 0
# while chk_idx < N:
#     if time == L[chk_idx][0]:
#         for i, com in enumerate(com_list):
#             if com == 0:
#                 com_list[i] = L[chk_idx][1]
#                 cnt_list[i] += 1
#                 break
#         else:
#             com_list.append(L[chk_idx][1])
#             cnt_list.append(1)
#         chk_idx += 1
#     for i, com in enumerate(com_list):
#         if com:
#             com_list[i] -= 1
#     time += 1
#
# print(len(cnt_list))
# for cnt in cnt_list:
#     if cnt:
#         print(cnt, end=' ')

# TLE 20%
from queue import PriorityQueue

N = int(input())
que = PriorityQueue()
for _ in range(N):
    tmp = list(map(int, input().split()))
    tmp[0], tmp[1] = tmp[1], tmp[0]
    que.put(tmp)

com_list = [0]
sort_list = [[]]
cnt_list = [[]]
while que.empty() == False:
    cur = que.get()
    for i, com in enumerate(com_list):
        if com <= cur[1]:
            com_list[i] = cur[0]
            cnt_list[i] += [cur[1]]
            if sort_list[i] and sort_list[i][1] < cur[1]:
                pass
            else:
                sort_list[i] = cur
            break
    else:  # 자리 없으면 만들기
        com_list.append(cur[0])
        sort_list.append(cur)
        cnt_list.append([cur[1]])

cnt_list = list(map(len, cnt_list))

for i in range(len(sort_list)):
    for j in range(i+1, len(sort_list)):
        if sort_list[i][1] > sort_list[j][1]:
            sort_list[i][1], sort_list[j][1] = sort_list[j][1], sort_list[i][1]
            cnt_list[i], cnt_list[j] = cnt_list[j], cnt_list[i]

print(len(cnt_list))
for cnt in cnt_list:
    print(cnt, end=' ')