import sys
sys.stdin = open('2636.txt', 'r')

R, C = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(R)]
CL = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        CL[i][j] = L[i][j]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

