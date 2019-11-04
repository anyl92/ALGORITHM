import sys
sys.stdin = open('16234.txt', 'r')

N, S, B = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
# print(N, S, B)
# print(L)
dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # j, i 상하좌우
res_cnt = 1


def bfs(j, i):
    global res_cnt, vst
    dq = [(j, i)]
    calc_list = [[j, i, L[i][j]]]
    while dq:
        for _ in range(len(dq)):
            j, i = dq.pop(0)
            vst[i][j] = res_cnt
            for d in dir:
                jj = j + d[0]
                ii = i + d[1]
                if 0 <= ii < N and 0 <= jj < N and vst[ii][jj] == 0:
                    if S <= abs(L[ii][jj] - L[i][j]) <= B:
                        dq.append([jj, ii])
                        vst[ii][jj] = res_cnt
                        calc_list += [[jj, ii, L[ii][jj]]]

    if len(calc_list) == 1:
        res_cnt = 0
        return []

    else:
        calc_sum = 0
        for calc in calc_list:
            calc_sum += calc[2]

        reset = calc_sum // len(calc_list)

        for calc in calc_list:
            calc[2] = reset

        res_cnt += 1
        return calc_list

    # print(calc_list)
    # print(vst)


def main():
    global res_cnt, vst
    total = []
    vst = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
             if not vst[i][j]:
                 total += bfs(j, i)
    print(total)

    for t in total:
        L[t[1]][t[0]] = t[2]
    print(L)

    print(max(map(max, vst)))
    print(res_cnt)

main()

