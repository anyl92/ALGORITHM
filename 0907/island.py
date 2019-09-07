import sys
sys.stdin = open('input.txt', 'r')

def BFS(start):
    aa = 0
    q = [start]
    visited = [[0]*M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    while q:
        c = q.pop(0)
        for d in dir:
            y = c[0]
            x = c[1]
            idy = y + d[0]
            idx = x + d[1]
            if 0 <= idx < M and 0 <= idy < N:
                if visited[idy][idx] == 0:
                    if L[idy][idx] == 'L':
                        visited[idy][idx] = visited[y][x] + 1
                        aa = visited[idy][idx]
                        q.append([idy, idx])
    if aa < 2:
        return 0
    return aa

N, M = map(int, input().split())  # 행, 열
L = [list(map(str, input())) for _ in range(N)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
a = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if L[i][j] == 'L':
            if BFS([i, j]) > a:
                a = BFS([i, j])
            cnt += 1
if cnt == 0:
    print(0)
else:
    print(a-1)