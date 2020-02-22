import sys
sys.stdin = open('3190.txt', 'r')

import collections

N = int(input())
A = int(input())
apple = [list(map(int, input().split())) for _ in range(A)]
T = int(input())
trans = [list(map(str, input().split())) for _ in range(T)]

L = [[0]*N for _ in range(N)]
for a in apple:
    L[a[0]-1][a[1]-1] = 1

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # rc
snake = collections.deque([[0, 0]])
d, time = 3, 0

while True:
    time += 1
    r, c = snake[0][0], snake[0][1]
    rr, cc = r + dir[d][0], c + dir[d][1]  # 이번 턴에 이동할 위치

    if rr < 0 or rr >= N or cc < 0 or cc >= N or L[rr][cc] == 2:  # 나가거나 뱀이면
        break

    if L[rr][cc] == 1:  # 다음자리에 사과가 !
        snake.appendleft((rr, cc))
        L[rr][cc] = 2
    if L[rr][cc] == 0:  # 없으묜
        snake.appendleft((rr, cc))
        L[rr][cc] = 2
        rrr, ccc = snake.pop()
        L[rrr][ccc] = 0

    if trans and time == int(trans[0][0]):  # 방향바꿔랏
        _, td = trans.pop(0)
        if td == 'L':
            if d == 0: d = 2
            elif d == 1: d = 3
            elif d == 2: d = 1
            elif d == 3: d = 0
        else:
            if d == 0: d = 3
            elif d == 1: d = 2
            elif d == 2: d = 0
            elif d == 3: d = 1
    r, c = rr, cc

print(time)