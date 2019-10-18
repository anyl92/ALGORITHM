import sys
sys.stdin = open('16236.txt', 'r')

import collections

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]


def find(i, j):
    global shark_size
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dq = collections.deque([i, j])
    fish = collections.deque('')
    V = [[0]*N for _ in range(N)]
    V[i][j] = 1
    time = 0

    while dq:  # dq가 있을때
        for _ in range(len(dq)):  # dq의 갯수만큼
            for d in dir:  # 4방향
                current = dq.popleft()
                print(current)
                ii = id + d[0]
                jj = jd + d[1]
                if 0 <= ii < N and 0 <= jj < N:  # 행렬 범위 내에서
                    if V[ii][jj] == 0:  # visited 아니면
                        if L[ii][jj] > shark_size:
                            continue  # 사이즈 크면 다음 방향으로
                        if L[ii][jj] == 0:
                            dq.append([ii, jj])  # 다음 dq볼 때
                            V[ii][jj] = 1  # visited 체크
                        if 0 < L[ii][jj] <= shark_size:
                            fish += (ii, jj)
                            dq.append([ii, jj])
                        print(fish)
            time += 1  # 이동거리 체크

    return



shark_size = 2

for i in range(N):
    for j in range(N):
        if L[i][j] == 9:
            find(i, j)

