import sys
sys.stdin = open('16234.txt', 'r')

import collections

N, S, B = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]


def bfs(j, i):
    global cnt, vst, calc_list
    # dq = collections.deque([])
    # calc_list = collections.deque([])
    # dq.append((j, i))
    dq = [(j, i)]
    vst[i][j] = 1
    # calc_list.append((j, i))
    calc_list = [(j, i)]
    calc_sum = L[i][j]

    while dq:
        (j, i) = dq.pop(0)
        for d in dir:
            jj, ii = j + d[0], i + d[1]
            if 0 <= ii < N and 0 <= jj < N and vst[ii][jj] == 0:
                if S <= abs(L[ii][jj] - L[i][j]) <= B:
                    dq.append((jj, ii))
                    vst[ii][jj] = 1
                    calc_list.append((jj, ii))
                    calc_sum += L[ii][jj]

    len_tmp = len(calc_list)
    if len_tmp == 1:
        calc_list = []
        return 0
    else:
        return calc_sum // len_tmp


dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # j, i 우하좌상
cnt = 0


while True:
    vst = [[0] * N for _ in range(N)]
    # or_list = collections.deque([])
    or_list = []
    if cnt > 2000:
        break

    for i in range(N):
        for j in range(N):
            if not vst[i][j]:
                return_value = bfs(j, i)
                if return_value:
                    for c in calc_list:
                        L[c[1]][c[0]] = return_value
                    or_list.append(True)
                else:
                    or_list.append(False)
    cnt += 1

    if not sum(or_list):
        break

print(cnt-1)