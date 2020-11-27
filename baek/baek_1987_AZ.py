import sys
sys.setrecursionlimit(10000)
sys.stdin = open('1987.txt', 'r')

R, C = map(int, input().split())
# L = [list(map(lambda x: ord(x)-65, sys.stdin.readline().strip())) for _ in range(R)]
L = [list(input()) for _ in range(R)]

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
V = [0 for _ in range(26)]
V[ord(L[0][0]) - 65] = 1
cnt = 1


def dfs(x=0, y=0, incnt=1):
    global cnt
    cnt = max(cnt, incnt)

    for dx, dy in direction:
        xx = x + dx
        yy = y + dy

        if 0 <= xx < C and 0 <= yy < R:
            cur = ord(L[yy][xx]) - 65
            if not V[cur]:
                V[cur] = 1
                dfs(xx, yy, incnt+1)
                V[cur] = 0


dfs()
print(cnt)


# cnt = 1
# max_cnt = 0
#
# while s:
#     x, y = s.popleft()
#     for dx, dy in direction:
#         xx = x+dx
#         yy = y+dy
#         if 0 <= xx < C and 0 <= yy < R:
#             cur = ord(L[yy][xx]) - 65
#             if V[cur]:
#                 if max_cnt < cnt:
#                     max_cnt = cnt
#                 continue
#             V[cur] = 1
#             s.append([xx, yy])
#     cnt += 1
#
#     for x in L:
#         print(x)
#     print(s)
#     print(V)
#     print(cnt)

