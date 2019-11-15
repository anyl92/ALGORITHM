import sys
sys.stdin = open('4008.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    O = list(map(int, input().split()))
    L = list(map(int, input().split()))

    opr = []
    for i in range(4):
        opr += [i] * O[i]

    minn = 10000000001
    maxx = -10000000001

    def solve(k):
        global maxx, minn
        if k == N - 1:
            tot = L[0]
            for i in range(1, N):
                if opr[i-1] == 0:  # +
                    tot += L[i]
                elif opr[i-1] == 1:  # -
                    tot -= L[i]
                elif opr[i-1] == 2:  # *
                    tot *= L[i]
                else:  # /
                    tot = int(tot / L[i])

            if tot < minn:
                minn = tot
            if tot > maxx:
                maxx = tot

        else:
            for i in range(k, N-1):
                opr[k], opr[i] = opr[i], opr[k]
                solve(k+1)
                opr[k], opr[i] = opr[i], opr[k]

    solve(0)
    print('#%d %d' % (tc, maxx-minn))