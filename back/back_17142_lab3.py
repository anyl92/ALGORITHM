import sys, collections, itertools
sys.stdin = open('17142.txt', 'r')

N, M = map(int, input().split())  # 크기 N, 바이러스 M
L = [list(map(int, input().split())) for _ in range(N)]
for k in L:
    print(k)


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
                    if L[yy][xx] == 0 and vst[yy][xx] == 0:
                        # L[yy][xx] = cnt
                        dq.append((xx, yy))
                        vst[yy][xx] = cnt
        cnt += 1

    for i in range(N):
        for j in range(N):
            if vst[i][j] == 0:
                min_cnt = -1
                return

    if min_cnt > cnt:
        min_cnt = cnt
    return


virus = collections.deque()  # 바이러스 append
vst = [[0] * N for _ in range(N)]  # visited, 함수 종료 처리

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # x, y 좌우상하
min_cnt = 9999999999

for i in range(N):
    for j in range(N):
        if L[i][j] == 2:  # 바이러스 좌표추가, vst
            virus.append((j, i))
            vst[i][j] = 1
        if L[i][j] == 1:  # 벽 vst
            vst[i][j] = 1

P = [i for i in range(len(virus))]
comb = list(itertools.combinations(P, M))
# print(comb)

# for k in vst:
#     print(k)

for j in range(len(comb)):
    dq = collections.deque()

    cvst = [[0] * N for _ in range(N)]  # vst copy
    for y in range(N):
        for x in range(N):
            cvst[y][x] = vst[y][x]
    # print(cvst)

    for i in range(M):
        dq.append(virus[comb[j][i]])
        # cvst[virus[comb[j][i]][0]][virus[comb[j][i]][1]] = 1
    bfs(dq, cvst)


print(min_cnt)