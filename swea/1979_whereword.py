import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]

    j, k, count, res = 0, 0, 0, 0
    for i in range(N):
        while j < N-K+1:
            k = 0
            if L[i][j] == 1:
                while k+j < N and L[i][j+k] == 1:
                    count += 1
                    k += 1
                j += count -1
            if count == K:
                res += 1
                count = 0
            j += 1
            count = 0
        j = 0

    i, k, count = 0, 0, 0
    for j in range(N):
        while i < N-K+1:
            k = 0
            if L[i][j] == 1:
                while k+i < N and L[i+k][j] == 1:
                    count += 1
                    k += 1
                i += count-1
            if count == K:
                res += 1
                count = 0
            i += 1
            count = 0
        i = 0
    print('#%d %d' % (tc, res))