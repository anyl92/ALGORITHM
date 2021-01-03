import sys
sys.stdin = open('2206.txt', 'r')

sys.setrecursionlimit(100000)

N, M = map(int, input().split())
L = [list(map(int, input())) for _ in range(N)]
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
V = [[[0, 0] for _ in range(M)] for _ in range(N)]
V[0][0] = 1




# def move(x, y, flag, c):
#     global cnt
#
#     if c > cnt or cnt == N+M-1:
#         return
#
#     for dx, dy in delta:
#         if x == M-1 and y == N-1:
#             cnt = min(cnt, c)
#             return
#
#         xx = dx + x
#         yy = dy + y
#         if 0 <= xx < M and 0 <= yy < N and not V[yy][xx]:
#             if flag and L[yy][xx]:  # 벽 깼는데 또 벽이다!
#                 continue
#             elif not flag and L[yy][xx]:  # 벽 처음 깬다!
#                 V[yy][xx] = 1
#                 move(xx, yy, 1, c+1)
#                 V[yy][xx] = 0
#             else:  # 벽 아니고 길임
#                 V[yy][xx] = 1
#                 move(xx, yy, flag, c+1)
#                 V[yy][xx] = 0
#
#
# cnt = 99999
# move(0, 0, 0, 1)
#
# if cnt == 99999 and not V[N-1][M-1]:
#     print(-1)
# else:
#     print(cnt)




# def move(move_list):
#     cnt = 0
#     while move_list:
#         cnt += 1
#         # if cnt == N*M*2:
#         #     break
#         x, y = move_list.popleft()
#         for dx, dy in delta:
#             xx = dx + x
#             yy = dy + y
#             if 0 <= xx < M and 0 <= yy < N:
#                 if xx == M-1 and yy == N-1:
#                     if cntL[yy][xx] and cntL[yy][xx] < cntL[y][x] + 1:
#                         continue
#
#                 if L[yy][xx] and not wallL[yy][xx] and wallL[y][x] < 2:  # 벽, 방문X, 벽1개
#                     move_list.append([xx, yy])
#                     wallL[yy][xx] = wallL[y][x] + 1
#                     cntL[yy][xx] = cntL[y][x] + 1
#                 elif not L[yy][xx]:  # 길
#                     if not cntL[yy][xx] or cntL[y][x] < cntL[yy][xx]:  # 방문X or 빠른경우
#                         move_list.appendleft([xx, yy])
#                         cntL[yy][xx] = cntL[y][x] + 1
#
#                 # if cntL[N-1][M-1]:
#                 #     return cntL[N-1][M-1]
#     return cntL[N-1][M-1]
#
#
# cntL[0][0] = 1
# if N == 1 and M == 1:
#     print(1)
# else:
#     res = move(mvl)
#     if res:
#         print(res)
#     else:
#         print(-1)
