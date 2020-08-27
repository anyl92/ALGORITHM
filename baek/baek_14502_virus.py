import sys
sys.stdin = open('14502.txt', 'r')


def virus_infact():
    q = []
    for i in range(virus_cnt):
        x, y = virus_pos[i]
        q.append((x, y))

        while q:
            x, y = q.pop(0)
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                idx = x + dx
                idy = y + dy
                if not (0 <= idx < N and 0 <= idy < M):
                    continue
                elif L[idx][idy] == 0:
                    L[idx][idy] = 2
                    q.append((idx, idy))


def count_safe_area():
    global ans
    tmp = sum(L, []).count(0)
    if ans < tmp:
        ans = tmp


def solve():
    wall = []
    for i in range(safe_cnt - 2):
        wall.append(i)
        for j in range(1 + i, safe_cnt - 1):
            wall.append(j)
            for k in range(j + 1, safe_cnt):
                wall.append(k)

                for l in range(3):
                    x, y = safe_pos[wall[l]]
                    L[x][y] = 1

                virus_infact()
                count_safe_area()

                for ii in range(N):
                    for jj in range(M):
                        L[ii][jj] = CL[ii][jj]

                wall.pop(-1)
            wall.pop(-1)
        wall.pop(-1)


N, M = map(int, input().split())
L = [0] * N
for i in range(N):
    L[i] = list(map(int, input().split()))
CL = [[0]*M for _ in range(N)]

virus_pos = [0] * 10
virus_cnt = 0

safe_pos = [0] * (N*M)
safe_cnt = 0

for i in range(N):
    for j in range(M):
        if L[i][j] == 2:
            virus_pos[virus_cnt] = (i, j)
            virus_cnt += 1
        elif L[i][j] == 0:
            safe_pos[safe_cnt] = (i, j)
            safe_cnt += 1
        CL[i][j] = L[i][j]

ans = 0
solve()
print(ans)