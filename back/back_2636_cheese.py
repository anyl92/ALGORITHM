import sys
sys.stdin = open('input.txt', 'r')

def bfs(L):
    global time, count
    q = [[0, 0]]
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        for _ in range(len(q)):
            current = q.pop(0)
            for k in range(4):
                y = current[0] + dy[k]
                x = current[1] + dx[k]
                if 0 <= y < N and 0 <= x < M:
                    if visited[y][x] == False:
                        if L[y][x] == 0:
                            q.append([y, x])
                            visited[y][x] = True
                        elif L[y][x] == 1:
                            L[y][x] = 2
                            visited[y][x] = True
    count = 0
    for i in range(N):
        for j in range(M):
            if L[i][j] == 2:
                count += 1
                L[i][j] = 0
    time += 1
N, M = map(int, input().split())  # 세로, 가로
L = [list(map(int, input().split())) for _ in range(N)]
copyL = [[0]*M for _ in range(N)]
time = 0
bfs(L)
while copyL != L:
    bfs(L)
print(time)
print(count)
