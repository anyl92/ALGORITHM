import sys
sys.stdin = open('3197.txt', 'r')

from collections import deque
R, C = map(int, input().split())
L = [list(map(str, input())) for _ in range(R)]

for r in range(R):
    for c in range(C):
        if L[r][c] == 'L':
            swan = [r, c]
            break

day = 1
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
V = [[0 for _ in range(C)] for _ in range(R)]


def kiss(start):
    global day, V
    q = deque()
    q.append(start)
    V[start[0]][start[1]] = day

    while q:
        r, c = q.popleft()
        for d in dir:
            rr, cc = r+d[0], c+d[1]
            if 0 <= rr < R and 0 <= cc < C and V[rr][cc] < day:
                if L[rr][cc] == 'L':
                    return True
                if L[rr][cc] == '.':
                    q.append([rr, cc])
                    V[rr][cc] = day
    return False


while True:
    res = kiss(swan)
    if res:
        print(day-1)
        break
    else:
        day += 1

    ice = deque()
    for r in range(R):
        for c in range(C):
            if L[r][c] == 'X':
                ice.append([r, c])

    melt_list = deque()
    for ir, ic in ice:
        for d in dir:
            irr, icc = ir + d[0], ic + d[1]
            if 0 <= irr < R and 0 <= icc < C:
                if L[irr][icc] != 'X':
                    melt_list.append([ir, ic])
                    break

    for m in melt_list:
        L[m[0]][m[1]] = '.'

    # for x in L:
    #     print(x)
    # print()