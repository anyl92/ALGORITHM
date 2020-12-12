import sys
sys.stdin = open('2665.txt', 'r')

import collections

N = int(input())
L = [list(map(int, input())) for _ in range(N)]
delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cntL = [[0 for _ in range(N)] for _ in range(N)]
V = [[0 for _ in range(N)] for _ in range(N)]


def move(o):
    move_list = collections.deque([])
    move_list.append(o)

    while move_list:
        x, y = move_list.popleft()
        for dx, dy in delta:
            xx = x+dx
            yy = y+dy
            if yy == xx == N-1:
                return cntL[y][x]
            if 0 <= xx < N and 0 <= yy < N and not V[yy][xx]:
                if L[yy][xx]:
                    move_list.appendleft([xx, yy])
                    cntL[yy][xx] = cntL[y][x]
                else:
                    move_list.append([xx, yy])
                    cntL[yy][xx] = cntL[y][x] + 1
                V[yy][xx] = 1


if N == 1 or sum(cntL, []) == 0:
    print(0)
else:
    print(move([0, 0]))