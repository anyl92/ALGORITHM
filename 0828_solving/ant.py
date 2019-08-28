import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    steps = 0

    for i in range(N):
        L[i].insert(0, 0)
        L[i].append(0)
    L.insert(0, [0]*(N+2))
    L.append([0]*(N+2))

    x, y = 1, 1
    i = 4
    while len(L)>x>0 and len(L)>y>0:
        if L[y][x] == 1:  # slash /
            if i == 1:  # 상
                i = 4
            elif i == 2:  # 하
                i = 3
            elif i == 3:  # 좌
                i = 2
            elif i == 4:  # 우
                i = 1
        elif L[y][x] == 2:  # reslash \
            if i == 1:
                i = 3
            elif i == 2:
                i = 4
            elif i == 3:
                i = 1
            elif i == 4:
                i = 2
        x += dx[i-1]
        y += dy[i-1]
        steps += 1

    if x == 0 or y == 0:
        print(steps - 1)
    else:
        print(steps - 2)