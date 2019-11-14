# 벽돌깨기
import sys
sys.stdin = open('5656.txt', 'r')

import collections


def copy_list():
    for i in range(H):
        for j in range(W):
            L[i][j] = CL[i][j]
    return


def locate(T):
    global min_bricks

    for r in T:  # 열, 구슬위치, x
        q = collections.deque([])
        V = [[0] * W for _ in range(H)]

        for c in range(H):  # 행, y
            if L[c][r]:
                q.append((r, c))
                break

        while q:
            x, y = q.popleft()
            repeat = L[y][x]
            L[y][x] = 0
            for d in dir:
                for i in range(1, repeat):
                    xx, yy = x + (i * d[0]), y + (i * d[1])
                    if 0 <= xx < W and 0 <= yy < H and not V[yy][xx]:
                        if L[yy][xx] > 1:
                            q.append((xx, yy))
                        else:
                            L[yy][xx] = 0
                        V[yy][xx] = 1

        for y in range(H-1, -1, -1):
            for x in range(W):
                y = H - 1
                cnt = 0
                while y > 0:
                    if not L[y][x]:  # 0이면
                        tmp = y
                        while not L[y - 1][x] and y >= 0:
                            y -= 1
                            cnt += 1
                        if y == 0:
                            cnt = 0
                            break
                        L[tmp][x] = L[y - 1][x]
                        L[y - 1][x] = 0
                        if cnt > 0:
                            y += cnt
                    y -= 1
                    cnt = 0

    bricks = 0
    for i in range(H):
        for j in range(W):
            if L[i][j]:
                bricks += 1
    if min_bricks > bricks:
        min_bricks = bricks

    copy_list()
    return


def comb(k):
    if k == N:
        locate((collections.deque(T)))
        return

    for i in range(W):
        T[k] = P[i]
        comb(k+1)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())  # 구슬, 가로(열), 세로(행)
    L = [list(map(int, input().split())) for _ in range(H)]
    CL = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            CL[i][j] = L[i][j]

    min_bricks = W*H
    T = [0]*N
    P = [i for i in range(W)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 좌우상하
    comb(0)

    print(min_bricks)
