import sys
sys.stdin = open('10026.txt', 'r')

N = int(input())

L = [list(input()) for _ in range(N)]
V = [[0 for _ in range(N)] for _ in range(N)]

NL = [['' for _ in range(N)] for _ in range(N)]
for a in range(N):
    for b in range(N):
        if L[a][b] == 'G':
            NL[a][b] = 'R'
        else:
            NL[a][b] = L[a][b]
NV = [[0 for _ in range(N)] for _ in range(N)]

cnt, cnt1 = 0, 0
delta = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def dfs(y, x, flag):
    if flag:
        V[y][x] = 1
    else:
        NV[y][x] = 1

    s = [[y, x]]
    while s:
        y, x = s.pop()
        for yy, xx in delta:
            yy += y
            xx += x
            if 0 <= xx < N and 0 <= yy < N:
                if flag:
                    if L[y][x] == L[yy][xx] and V[yy][xx] == 0:
                        V[yy][xx] = 1
                        s.append([yy, xx])
                else:
                    if NL[y][x] == NL[yy][xx] and NV[yy][xx] == 0:
                        NV[yy][xx] = 1
                        s.append([yy, xx])


for i in range(N):
    for j in range(N):
        if V[i][j] == 0:
            cnt1 += 1
            dfs(i, j, 1)

for i in range(N):
    for j in range(N):
        if NV[i][j] == 0:
            cnt += 1
            dfs(i, j, 0)

print(cnt1, cnt)

