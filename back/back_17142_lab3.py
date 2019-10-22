import sys, collections, itertools
sys.stdin = open('17142.txt', 'r')

N, M = map(int, input().split())  # 크기 N, 바이러스 M
L = [list(map(int, input().split())) for _ in range(N)]
print(L)

virus = collections.deque()

for i in range(N):
    for j in range(N):
        if L[i][j] == 2:
            virus.append((i, j))
print(virus)

P = [i for i in range(len(virus))]
comb = list(itertools.combinations(P, M))
print(comb)

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
min_cnt = 9999999999

def bfs(dq, vst):
    global min_cnt
    cnt = 1

    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            print(x, y)
            for d in dir:
                xx = x + d[0]
                yy = y + d[1]
                if 0 <= xx < N and 0 <= yy < N:
                    if L[xx][yy] == 0 and vst[xx][yy] == 0:
                        L[xx][yy] = cnt
                        dq.append((xx, yy))
                        vst[xx][yy] = 1
        cnt += 1

    if min_cnt > cnt:
        min_cnt = cnt
    return


for j in range(len(comb)):
    dq = collections.deque()
    vst = [[0] * N for _ in range(N)]
    for i in range(3):
        dq.append(virus[comb[j][i]])
        vst[virus[comb[j][i]][0]][virus[comb[j][i]][1]] = 1
    bfs(dq, vst)

print(min_cnt)