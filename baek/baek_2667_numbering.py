import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
L = [list(map(int, input())) for _ in range(N)]
vst = [[0 for _ in range(N)] for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(i, j):
    q = [[i, j]]
    home = 1
    while q:
        i, j = q.pop()
        for d in dir:
            ii, jj = i + d[0], j + d[1]
            if 0 <= ii < N and 0 <= jj < N and not vst[ii][jj]:
                if L[ii][jj]:
                    L[ii][jj] = 0
                    q.append([ii, jj])
                    vst[ii][jj] = 1
                    home += 1
    return home


cnt = 0
home = []
for i in range(N):
    for j in range(N):
        if L[i][j] and not vst[i][j]:
            vst[i][j] = 1
            home += [bfs(i, j)]
            cnt += 1

print(cnt)
for h in sorted(home):
    print(h)
