import sys
sys.stdin = open('2636.txt', 'r')

R, C = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(R)]

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
time = 0


def air(i, j):
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


while True:
    air(0, 0)  # 치즈 바깥 부분 2로 바꾸기

    for i in range(R):
        for j in range(C):
            if L[i][j] == 2:
                for d in dir:
                    ii, jj = i + d[0], j + d[1]
                    if 0 <= ii < R and 0 <= jj < C:
                        if L[ii][jj] == 1:
                            L[ii][jj] = 3
                            continue

    cnt = 0
    for i in range(R):
        for j in range(C):
            if L[i][j] == 3:
                cnt += 1
                L[i][j] = 0
            if L[i][j] == 2:
                L[i][j] = 0
    time += 1

    if not sum(L, []).count(1):
        break

print(time)
print(cnt)