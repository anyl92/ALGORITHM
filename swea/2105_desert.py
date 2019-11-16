import sys
sys.stdin = open('2105.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    dir = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # i행,j열 / 하우 하좌 상좌 상우
    vst = [[0 for _ in range(N)] for _ in range(N)]

    # def dfs(i, j):
    #     s = [(i, j)]
    #     vst = [[0 for _ in range(N)] for _ in range(N)]
    #     vst[i][j] = 1
    #     route = [L[i][j]]
    #
    #     while s:
    #         i, j = s.pop()
    #         for d in dir:
    #             ii, jj = i+d[0], j+d[1]
    #             if 0 <= ii < N and 0 <= jj < N and not vst[ii][jj]:
    #                 if i == ii and j == jj:
    #                     return len(route)
    #                 if L[ii][jj] not in route:
    #                     s.append((ii, jj))
    #                     vst[ii][jj] = 1
    #                     route += [L[ii][jj]]
    #                 else:
    #                     continue
    #     return


    def recul(i, j):
        global chk, flag
        ii, jj = i + dir[flag][0], j + dir[flag][1]

        if ii == i and jj == j:
            return

        if not (0 <= ii < N and 0 <= jj < N):
            flag += 1
            return

        recul(ii, jj)
        recul(ii, jj)
        return


    chk = []
    for i in range(N-2):
        for j in range(1, N-1):
            flag = 0
            print(recul(i, j))

