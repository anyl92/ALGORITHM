import sys
sys.stdin = open('4008.txt', 'r')

import itertools

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    O = list(map(int, input().split()))
    L = list(map(int, input().split()))

    opr = []
    for i in range(len(O)):
        for j in range(O[i]):
            opr += [i]
    # print(opr)

    perm = set(list(itertools.permutations(opr, N-1)))
    # print(perm)

    minn = 10000000001
    maxx = -10000000001

    for p in perm:
        tot = L[0]
        j = 0
        for i in range(1, N):
            op = p[j]
            if op == 0:  # +
                tot += L[i]
            if op == 1:  # -
                tot -= L[i]
            if op == 2:  # *
                tot *= L[i]
            if op == 3:  # /
                if L[i] == 0:
                    break
                if tot <= 0:
                    tot = 0 - (abs(tot) // L[i])
                else:
                    tot //= L[i]
            j += 1

        if tot < minn:
            minn = tot
        if tot > maxx:
            maxx = tot

    print('#%d %d' % (tc, maxx-minn))