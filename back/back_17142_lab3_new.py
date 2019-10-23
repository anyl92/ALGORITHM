# 최적화를 시키려고 했는데 왜 시간이 늘었을까

import sys
sys.stdin = open('17142.txt', 'r')

import collections, itertools

N, M = map(int, input().split())  # 크기 N, 바이러스 M
L = [list(map(int, input().split())) for _ in range(N)]


def bfs(dq, vst):
    global min_cnt, lose_virus
    cnt = 1

    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for d in dir:
                xx, yy = x + d[0], y + d[1]
                if 0 <= xx < N and 0 <= yy < N:
                    if vst[yy][xx] == 0:
                        dq.append((xx, yy))
                        if L[yy][xx] == 2:
                            vst[yy][xx] = 1
                            continue
                        vst[yy][xx] = cnt
        cnt += 1

    for i in range(N):
        for j in range(N):
            if vst[i][j] == 0:
                lose_virus += 1
                return

    cnt = max(map(max, vst))

    if min_cnt > cnt:
        min_cnt = cnt
    return


def main():
    zero_cnt = 0
    virus = collections.deque()  # 바이러스 append
    vst = [[0] * N for _ in range(N)]  # visited, 함수 종료 처리

    for i in range(N):
        for j in range(N):
            if L[i][j] == 2:  # 바이러스 좌표추가, vst
                virus.append((j, i))
            if L[i][j] == 1:  # 벽 vst
                vst[i][j] = 1
            if L[i][j] == 0:
                zero_cnt += 1

    if zero_cnt:
        P = [i for i in range(len(virus))]
        comb = list(itertools.combinations(P, M))

        for j in range(len(comb)):  # 조합 총개수 => 경우의수 만큼 for
            dq = collections.deque()
            cvst = [[0] * N for _ in range(N)]  # vst copy
            for y in range(N):
                for x in range(N):
                    cvst[y][x] = vst[y][x]

            for i in range(M):  # 바이러스 총개수 => 뽑힌 조합으로 dq에 추가
                dq.append(virus[comb[j][i]])
                cvst[virus[comb[j][i]][1]][virus[comb[j][i]][0]] = 1
            bfs(dq, cvst)
    else:
        return 0

    if lose_virus == len(comb):
        return -1
    else:
        return min_cnt


dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # x, y 좌우상하
min_cnt = 9999999999
lose_virus = 0

print(main())