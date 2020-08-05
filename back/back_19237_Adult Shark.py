import sys
sys.stdin = open('19237.txt', 'r')

N, M, k = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
d = list(map(int, input().split()))
P = [[] for _ in range(M)]
for m in range(M):
    for _ in range(4):
        P[m] += [list(map(int, input().split()))]

# 초기배열
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
smell = [[[] for _ in range(N)] for _ in range(N)]
move = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if L[i][j]:
            cur = L[i][j]
            smell[i][j] = [cur, k]
            L[i][j] = [cur, d[cur-1]]
time = 0

while True:
    if time > 1000:
        print(-1)
        break

    # 이동하기
    for i in range(N):
        for j in range(N):
            if L[i][j]:
                cur_n = L[i][j][0]
                cur_d = L[i][j][1]
                cur_p = P[cur_n - 1][cur_d - 1]

                onego_list, twogo_list = [], []
                for p in cur_p:
                    idx, jdx = dir[p-1]
                    if 0 <= i+idx < N and 0 <= j+jdx < N:
                        if smell[i+idx][j+jdx] == []:
                            onego_list += [[i + idx, j + jdx, p]]
                            break
                        elif smell[i+idx][j+jdx][0] == cur_n:
                            twogo_list += [[i + idx, j + jdx, p]]

                if onego_list != []:
                    ii, jj, pp = onego_list.pop(0)
                else:
                    ii, jj, pp = twogo_list.pop(0)

                if move[ii][jj]:
                    cur = move[ii][jj]
                    new = L[i][j]
                    if cur[0] < new[0]:
                        move[ii][jj] = [cur[0], pp]
                    else:
                        move[ii][jj] = [new[0], pp]
                else:
                    move[ii][jj] = [L[i][j][0], pp]
                move[i][j] = []

    # 냄새빼기
    for a in range(N):
        for b in range(N):
            if smell[a][b]:
                smell[a][b][1] -= 1
                if smell[a][b][1] == 0:
                    smell[a][b] = []

    # 배열복사 냄새깔기
    L = [[0 for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if move[a][b]:
                L[a][b] = move[a][b]
                smell[a][b] = [move[a][b][0], k]

    time += 1

    x_list = []
    for x in sum(L, []):
        if x:
            x_list += [x[0]]
    if len(x_list) == 1 and x_list[0] == 1:
        print(time)
        break
