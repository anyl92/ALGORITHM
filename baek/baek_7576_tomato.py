import sys
sys.stdin = open('7576.txt', 'r')

from collections import deque

# T = int(input())
# for tc in range(1, T+1):
C, R = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(R)]


def check(day):
    for r in range(R):
        for c in range(C):
            if L[r][c] == 0:
                return 1
    return 0


day = 1
flag = 0
def bfs(q):
    global day, flag
    v = [[0]*C for _ in range(R)]
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            v[y][x] = 1 
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                xx, yy = x+dx, y+dy
                if 0 <= xx < C and 0 <= yy < R:
                    if v[yy][xx] == 0 and L[yy][xx] == 0:
                        v[yy][xx] = 1
                        L[yy][xx] = 1
                        q.append((xx, yy))
        # for x in v:
        #     print(x)
        # print('day')
        # print(q)
        # for z in L:
        #     print(z)
        # chk = check(day)
        if check(day) == 0:
            flag = 1
            return day
        else:
            day += 1
    return day


zerocnt = 0
bfs_list = deque()
for r in range(R):
    for c in range(C):
        if L[r][c] == 1:
            bfs_list.append((c, r))
        if L[r][c] == 0:
            zerocnt += 1
# print(bfs_list)            

if zerocnt:
    tmp = bfs(bfs_list)
    if flag:
        print(tmp)
    else:
        print(-1)
else:
    print(0)