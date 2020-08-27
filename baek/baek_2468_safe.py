import sys
sys.stdin = open('2468.txt', 'r')

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
CL = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        CL[i][j] = L[i][j]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(i, j):
    q = [[i, j]]
    while q:
        i, j = q.pop(0)
        for d in dir:
            ii, jj = i + d[0], j + d[1]
            if 0 <= ii < N and 0 <= jj < N and not vst[ii][jj]:
                if L[ii][jj]:
                    vst[ii][jj] = 1
                    q.append([ii, jj])
    return 1


chk_val = max(map(max, L))
res = 0

for chk in range(chk_val+1):
    vst = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if L[i][j] <= chk:
                L[i][j] = 0

    cnt = 0
    for i in range(N):
        for j in range(N):
            if L[i][j] and not vst[i][j]:
                vst[i][j] = 1
                cnt += bfs(i, j)

    if res < cnt:
        res = cnt

    for i in range(N):
        for j in range(N):
            L[i][j] = CL[i][j]

print(res)