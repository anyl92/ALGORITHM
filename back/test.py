import sys
sys.stdin = open('16234.txt', 'r')

import collections

N, S, B = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # j, i 상하좌우
cnt = 0


def bfs(j, i):
    global cnt, vst, calc_list
    dq = collections.deque([])
    calc_list = collections.deque([])
    dq.append((j, i))
    vst[i][j] = 1
    calc_list.append((j, i, L[i][j]))
    while dq:
        for _ in range(len(dq)):
            (j, i) = dq.popleft()
            for d in dir:
                jj = j + d[0]
                ii = i + d[1]
                if 0 <= ii < N and 0 <= jj < N and vst[ii][jj] == 0:
                    if S <= abs(L[ii][jj] - L[i][j]) <= B:
                        dq.append((jj, ii))
                        vst[ii][jj] = 1
                        calc_list.append((jj, ii, L[ii][jj]))

    if len(calc_list) == 1:
        return -2

    else:
        calc_sum = 0
        for calc in calc_list:
            calc_sum += calc[2]
        reset = calc_sum // len(calc_list)

        return reset


def main(L):
    global cnt, vst, calc_list
    vst = [[0] * N for _ in range(N)]
    or_list = collections.deque([])

    if cnt > 2000:
        return

    for i in range(N):
        for j in range(N):
             if not vst[i][j]:
                 return_value = bfs(j, i)
                 if return_value == -2:
                     or_list.append(False)
                 else:
                     or_list.append(True)
                     for t in calc_list:
                         L[t[1]][t[0]] = return_value
    cnt += 1

    if sum(or_list):
        main(L)
        return 0
    else:
        return 0

main(L)
print(cnt-1)