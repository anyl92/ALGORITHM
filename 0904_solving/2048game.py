import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())
    N = int(N)
    L = [list(map(int, input().split())) for _ in range(int(N))]
    print(N, M, L)

    j, k, cnt = 0, 0, 0
    for i in range(N):
        while j < (N-1):
            if L[i][j] == 0:
                k = j
                while L[i][j+1] == 0 and j < N:
                    j += 1
                    cnt += 1
                L[i][k] = L[i][j]
                L[i][j] = 0
            j += 1
        j = 0
    print(L)