import sys
sys.stdin = open('7569.txt', 'r')

from collections import deque

M, N, H = map(int, input().split())  # 가로 세로 높이
L = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]


def check(day):
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if L[z][y][x] == 0:
                    return 1  # 더 돌아
    return 0  # while 종료


day = 1
dir = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]
def bfs(q):
    global day
    v = [[[0]*M for _ in range(N)] for _ in range(H)]
    while q:
        for _ in range(len(q)):
            x, y, z = q.popleft()
            for d in dir:
                xx, yy, zz = x+d[0], y+d[1], z+d[2]
                if 0 <= xx < M and 0 <= yy < N and 0 <= zz < H:
                    if v[zz][yy][xx] == 0 and L[zz][yy][xx] == 0:
                        v[zz][yy][xx] = 1
                        L[zz][yy][xx] = 1
                        q.append((xx, yy, zz))
        chk = check(day)
        if chk == 0:
            return day  # 0없으니 나가서 day나 세라
        else:
            day += 1  # 하루가 지나염
    return -1  # 0이 있어 ...


zero_cnt = 0
bfs_list = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if L[z][y][x] == 1:
                bfs_list.append((x, y, z))
            if L[z][y][x] == 0:
                zero_cnt += 1

if zero_cnt:
    print(bfs(bfs_list))
else:
    print(0)
