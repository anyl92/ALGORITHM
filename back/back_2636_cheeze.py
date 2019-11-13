import sys
sys.stdin = open('2636.txt', 'r')

R, C = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(R)]
CL = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        CL[i][j] = L[i][j]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
time = 0


def dfs(i, j):
    vst = [[0 for _ in range(C)] for _ in range(R)]
    vst[i][j] = 1
    L[i][j] = 2
    s = [[i, j]]

    while s:
        i, j = s.pop()
        for d in dir:
            ii, jj = i+d[0], j+d[1]
            if 0 <= ii < R and 0 <= jj < C:
                if L[ii][jj] == 0:
                    L[ii][jj] = 2
                    s.append([ii, jj])


dfs(0, 0)  # 치즈 바깥 부분 2로 바꾸기

for l in L:
    print(l)
print()

air = 2
while True:
    for i in range(R):
        for j in range(C):
            if L[i][j] == air:
                for d in dir:
                    ii, jj = i + d[0], j + d[1]
                    if 0 <= ii < R and 0 <= jj < C:
                        if L[ii][jj] == 1:
                            L[ii][jj] = air
                            continue

    for l in L:
        print(l)
    print()

    cnt = 0
    for i in range(R):
        for j in range(C):
            if L[i][j] == 1:
                cnt += 1

    if cnt == 0:
        break

print(cnt)