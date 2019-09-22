import sys
sys.stdin = open('input.txt', 'r')

def perm(k, tmp=0):
    global res
    if k == N:
        if tmp < res:
            res = tmp
    else:
        if tmp > res:
            return 0
        for i in range(N):
            if not V[i]:
                V[i] = 1
                tmp += L[k][i]
                perm(k+1, tmp)
                tmp -= L[k][i]
                V[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    V = [0] * (N)
    res = 999999
    perm(0)
    print('#%d %d' % (tc, res))