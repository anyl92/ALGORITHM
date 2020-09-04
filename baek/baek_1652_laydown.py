import sys
sys.stdin = open('1652.txt', 'r')

N = int(input())
L = [list(map(str, input())) for _ in range(N)]
orig_L = [[0 for _ in range(N)] for _ in range(N)]
curl_L = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if L[i][j] == '.':
            orig_L[i][j] = 0
            curl_L[j][N-1-i] = 0
        else:
            orig_L[i][j] = 1
            curl_L[j][N-1-i] = 1

garo, sero = 0, 0
# 가로
for i in range(N):
    j = 0
    while j < N-1:
        if orig_L[i][j] == 0 and orig_L[i][j+1] == 0:
            while j < N-1 and orig_L[i][j] != 1:
                j += 1
            garo += 1
        j += 1
# 세로
for i in range(N):
    j = 0
    while j < N-1:
        if curl_L[i][j] == 0 and curl_L[i][j+1] == 0:
            while j < N-1 and curl_L[i][j] != 1:
                j += 1
            sero += 1
        j += 1
print(garo, sero)