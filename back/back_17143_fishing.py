import sys
sys.stdin = open('17143.txt', 'r')

R, C, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
# r, c, 속력 s, 1위 2아래 3오른 4왼 d, 크기 z

getsum = 0
dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def eat(L):
    for r in range(R):
        for c in range(C):
            if len(L[r][c]) >= 2:
                L[r][c] = sorted(L[r][c], key=lambda x: x[2])
                # print(L[r][c], '정렬된상어')
                while len(L[r][c]) != 1:
                    s, d, z = L[r][c].pop(0)
                    info.remove([r+1, c+1, s, d, z])
                # print(L[r][c], '됐냐?')
                # for k in range(len(L[r][c])-1):
                #     print(L[r][c][k])
                # L[r][c] = [L[r][c][-1]]
                # info.remove([r + 1, c + 1, L[r][c][0][0], L[r][c][0][1], L[r][c][0][2]])


def reset():
    L = [[[] for _ in range(C)] for _ in range(R)]
    # print(info, 'info')
    for i in info:
        # print(i)
        L[i[0] - 1][i[1] - 1].append((i[2], i[3], i[4]))
    return L


def move(L):
    for shark in info:
        y, x, s, d, _ = map(int, shark)  # 현재 rcs
        if d == 1 or d == 2:
            s = s % (2 * (R - 1))
        else:
            s = s % (2 * (C - 1))

        for _ in range(s):
            # dy, dx = shark[0] + dir[shark[3] - 1][0], shark[1] + dir[shark[3] - 1][1]
            if d < 3:
                if shark[0] == 1 and shark[3] == 1:
                    shark[3] = 2
                elif shark[0] == R and shark[3] == 2:
                    shark[3] = 1

                if shark[3] == 1:
                    shark[0] -= 1
                elif shark[3] == 2:
                    shark[0] += 1

            else:
                if shark[1] == 1 and shark[3] == 4:
                    shark[3] = 3
                elif shark[1] == C and shark[3] == 3:
                    shark[3] = 4

                if shark[3] == 3:
                    shark[1] += 1
                elif shark[3] == 4:
                    shark[1] -= 1


L = reset()
if info:
    for c in range(C):
        for r in range(R):
            if L[r][c]:
                getsum += L[r][c][0][2]  # 상어잡기
                info.remove([r + 1, c + 1, L[r][c][0][0], L[r][c][0][1], L[r][c][0][2]])
                L[r][c] = []  # 상어꺼내
                break
        move(L)
        # for x in L:
        #     print(x)
        # print()
        L = reset()
        eat(L)
    print(getsum)
else:
    print(0)