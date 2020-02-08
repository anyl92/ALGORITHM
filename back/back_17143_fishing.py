import sys
sys.stdin = open('17143.txt', 'r')

from collections import deque

R, C, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
# r, c, 속력 s, 1위 2아래 3오른 4왼 d, 크기 z

getsum = 0
dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def eat(L):
    for r in range(R):
        for c in range(C):
            if len(L[r][c]) >= 2:
                L[r][c] = sorted(L[r][c], key=lambda x:x[2])
                L[r][c] = [L[r][c][-1]]


def reset():
    L = [[[] for _ in range(C)] for _ in range(R)]
    for i in info:
        L[i[0]-1][i[1]-1].append((i[2], i[3], i[4]))
    return L


def move(L):
    for shark in info:
        y, x, s, d, z = map(int, shark)  # 현재 rcs
        s = s % (2 * (R - 1))
        # if d == 1:  # 위
        #     if (y - 1) < s:
        #         if (s // R) % 2:
        #             shark[3] = 2
        #             shark[0] = y + (s % R)
        #         else:
        #             shark[0] = y - (s % R)
        #     else:
        #         shark[0] = y - s
        # elif d == 2:  # 아래
        #     if (R - y) < s:
        #         if (s // R) % 2:
        #             shark[3] = 1
        #             shark[0] = y - (s % R)
        #         else:
        #             shark[0] = y + (s % R)
        #     else:
        #         shark[0] = y + s
        # elif d == 3:  # 오른
        #     if (C - x) < s:
        #         if (s // C) % 2:
        #             shark[3] = 4
        #             shark[1] = x - (s % C)
        #         else:
        #             shark[1] = x + (s % C)
        #     else:
        #         shark[1] = x + s
        # elif d == 4:  # 왼
        #     if (x - 1) < s:
        #         if (s // C) % 2:
        #             shark[3] = 3
        #             shark[1] = x + (s % C)
        #         else:
        #             shark[1] = x - (s % C)
        #     else:
        #         shark[1] = x - s

        for _ in range(s):
            d = dir[shark[3]-1]
            dy, dx = y+d[0], x+d[1]
            if not (0 < dy <= R and 0 < dx <= C):
                if shark[3] % 2:
                    shark[3] += 1
                else:
                    shark[3] -= 1
                d = dir[shark[3]-1]
                dy, dx = y+d[0], x+d[1]
            y, x = dy, dx  # 다음 자리로 업뎃
        shark[0], shark[1] = y, x  # info 정보도 업뎃


L = reset()
if info:
    for c in range(C):
        for r in range(R):
            if L[r][c]:
                getsum += L[r][c][0][2]  # 상어잡기
                info.remove([r+1, c+1, L[r][c][0][0], L[r][c][0][1], L[r][c][0][2]])
                L[r][c] = []  # 상어꺼내
                break
        move(L)
        L = reset()
        eat(L)
    print(getsum)
else:
    print(0)