import sys
sys.stdin = open('7576.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    C, R = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(R)]
    print(C, R, L)

    def check(day):
        for r in range(R):
            for c in range(C):
                if L[r][c] == 0:
                    return day + 1
        return -1

    day = 0
    flag = 0
    def bfs(c, r, day):
        q = [(c, r)]
        v = [[0]*C for _ in range(R)]
        v[r][c] = 1
        while q:
            for _ in range(len(q)):
                x, y = q.pop(0)
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    xx, yy = x+dx, y+dy
                    if 0 <= xx < C and 0 <= yy < R:
                        if v[yy][xx] == 0 and L[yy][xx] == 0:
                            v[yy][xx] = 1
                            L[yy][xx] = 1
                            q.append((xx, yy))
            # print('day')
            # print(q)
            # for z in L:
            #     print(z)
            chk = check(day)
            if chk == -1:
                flag = 1
                return day
            else:
                day = chk
        return day


    for r in range(R):
        for c in range(C):
            if L[r][c] == 1:
                # print('in', r, c)
                tmp = bfs(c, r, 1)
                if tmp > day:
                    day = tmp

    for z in L:
        print(z)
    print(flag)
    if flag:
        print(day)
    else:
        print(-1)