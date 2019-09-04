import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = [[0]*N for _ in range(N)]

    for i in range(N):
        C[i][0] = 1
        C[i][i] = 1

    for i in range(2, N):
        for j in range(1, N):
            C[i][j] = C[i-1][j] + C[i-1][j-1]

    print('#%d' % (tc))
    for i in range(N):
        for j in range(N):
            if not C[i][j]:
                continue
            else:
                print(C[i][j], end=' ')
        print()