import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [str(input()) for _ in range(N)]

    count, res, i = 0, 0, 0
    f = 0
    j = N//2  # 2
    while count < N:
        for k in range(j, j+1+(i*2)):
            res += int(L[count][k])
        if f:
            j += 1
            i -= 1
        else:
            j -= 1
            i += 1
        count += 1
        if j == 0:
            f = 1
    print('#%d %d' % (tc, res))