import sys
sys.stdin = open('15683.txt', 'r')

import collections

for _ in range(6):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M)
    # print(L)

    dir = [
        [[(1, 0)], [(-1, 0)], [(0, -1)], [(0, 1)]],  # 0 우좌상하
        [[(1, 0), (-1, 0)], [(0, -1), (0, 1)]],      # 1
        [[(1, 0), (0, -1)], [(1, 0), (0, 1)],
         [(-1, 0), (0, 1)], [(-1, 0), (0, -1)]],     # 2
        [[(1, 0), (-1, 0), (0, -1)], [(-1, 0), (0, -1), (0, 1)],
         [(1, 0), (-1, 0), (0, 1)], [(1, 0), (0, -1), (0, 1)]],  # 3
        [[(1, 0), (-1, 0), (0, -1), (0, 1)]]         # 4
    ]
    cnt = 0
    square = N*M


    def watch(cctv):
        global square
        tmp = 70

        for cctv in dir[cctv_num]:
            vst = [[0 for _ in range(M)] for _ in range(N)]
            csq = square
            cnt = 0
            for d in cctv:
                while 0 <= x+d[0] < M and 0 <= y+d[1] < N:
                    x, y = x + d[0], y + d[1]
                    if L[y][x] == 6:
                        break
                    if not vst[y][x]:
                        vst[y][x] = 1
                        cnt += 1
            if tmp > csq - cnt:
                tmp = csq - cnt
        return print(tmp)


    cctv = collections.deque([])
    for y in range(N):
        for x in range(M):
            if L[y][x] == 6:
                square -= 1
                continue
            if L[y][x]:
                square -= 1
                cctv += (x, y, L[y][x]-1)
    watch(cctv)
