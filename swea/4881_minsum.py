# 4881
import sys
sys.stdin = open('minsum_input.txt', 'r')


def func(idx, summ):
    global res
    if summ > res:
        return
    if idx == N:
        res = summ
    else:
        for i in range(N):
            if V[i]:
                continue
            V[i] = 1
            func(idx + 1, summ + M[idx][i])
            V[i] = 0


V = [0 for _ in range(10)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    res = 99
    func(0, 0)
    print('#%d %d' % (tc, res))