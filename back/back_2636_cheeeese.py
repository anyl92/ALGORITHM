import sys
sys.stdin = open('input.txt', 'r')

def bfs(L):
    global time, count
    while sum(sum(L, [])) != 0:
        q = [[0, 0]]
        visited = [[False]*garo for _ in range(sero)]
        visited[0][0] = True
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            for _ in range(len(q)):
                c = q.pop(0)
                for d in dir:
                    y = c[0]
                    x = c[1]
                    idy = y + d[0]
                    idx = x + d[1]
                    if 0 <= y < sero and 0 <= x < garo:
                        if visited[y][x] == False:
                            if L[y][x] == 0:
                                q.append([y, x])
                                visited[y][x] = True
                            elif L[y][x] == 1:
                                L[y][x] = 2
                                visited[y][x] = True
        count = 0
        for i in range(sero):
            for j in range(garo):
                if L[i][j] == 2:
                    count += 1
                    L[i][j] = 0
        time += 1

sero, garo = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(sero)]
count, time = 0, 0
bfs(L)
print(time)
print(count)
