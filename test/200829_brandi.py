# 1
user_age, max_heartrate = 0, 0
print_list = [0 for _ in range(6)]  # 최고, 고, 중, 집중, 워밍, 휴식

while True:
    if user_age:

        try:
            cur = float(input())
        except EOFError:
            break

        if max_heartrate * 90 / 100 <= cur:
            print_list[0] += 1
        elif max_heartrate * 80 / 100 <= cur:
            print_list[1] += 1
        elif max_heartrate * 75 / 100 <= cur:
            print_list[2] += 1
        elif max_heartrate * 68 / 100 <= cur:
            print_list[3] += 1
        elif max_heartrate * 60 / 100 <= cur:
            print_list[4] += 1
        else:
            print_list[5] += 1

    else:  # 없으면
        user_age = int(input())
        max_heartrate = 220 - user_age

for e in print_list:
    print(e, end=' ')


# 2
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
CL = [[0 for _ in range(N)] for _ in range(N)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
L[0][0] = 2  # 물
L[N-1][N-1] = 7  # 홍현

time, res = 0, 0
water = [(0, 0)]
cur_p_loca = [(N - 1, N - 1)]


def splash(L, water):
    cnt = 0
    cur_water = []
    for x in water:
        cur_water.append(x)

    while cur_water:
        i, j = cur_water.pop(0)
        for ii, jj in dir:
            ii = ii + i
            jj = jj + j
            if 0 <= ii < N and 0 <= jj < N:
                if L[ii][jj] == 0 or L[ii][jj] == 7:
                    L[ii][jj] = 2
                    cur_water.append((ii, jj))

    for y in range(N):
        for x in range(N):
            if L[y][x] == 0 or L[y][x] == 7:
                cnt += 1
    return cnt


while cur_p_loca:
    new_water = []
    while water:
        a, b = water.pop(0)
        for aa, bb in dir:
            aa = aa+a
            bb = bb+b
            if 0 <= aa < N and 0 <= bb < N:
                if L[aa][bb] == 0 or L[aa][bb] == 7:
                    L[aa][bb] = 2
                    new_water.append((aa, bb))
    water = new_water

    i, j = cur_p_loca.pop(0)
    for ii, jj in dir:
        ii = ii+i
        jj = jj+j
        if 0 <= ii < N and 0 <= jj < N:
            if L[ii][jj] == 0:
                L[ii][jj] = 3

                for y in range(N):
                    for x in range(N):
                        CL[y][x] = L[y][x]

                cnt = splash(CL, water)
                if cnt > res:
                    res = cnt

                L[ii][jj] = 7
                cur_p_loca.append((ii, jj))

            elif L[ii][jj] == 1:
                L[ii][jj] = 8
                cur_p_loca.append((ii, jj))
print(res)