import sys
sys.stdin = open('1783.txt', 'r')

N, M = map(int, input().split())  # 세로y 가로x
L = [[0 for _ in range(M)] for _ in range(N)]
L[N-1][0] = 1
dir = [(-2, 1), (-1, 2), (1, 2), (2, 1)]  # y x

# print(L[0][N-1])
for l in L:
    print(l)

q = [(N-1, 0)]
while q:
    for _ in range(q):
        y, x = q.pop
        for yy, xx in dir:
            ydx, xdx = y+yy, x+xx
            if 0 < ydx < N and 0 < xdx < M:
                L[ydx][xdx]