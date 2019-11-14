import sys
sys.stdin = open('4012.txt', 'r')

import itertools

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    T = [i for i in range(N)]
    comb = list(itertools.combinations(T, N//2))

    res = 99999
    for i in range(len(comb)//2):
        current = [comb[i], comb[-1-i]]

        comb1 = list(itertools.combinations(current[0], 2))
        synergy1 = 0
        for r, c in comb1:
            synergy1 += abs(L[r][c] + L[c][r])

        comb2 = list(itertools.combinations(current[1], 2))
        synergy2 = 0
        for r, c in comb2:
            synergy2 += abs(L[r][c] + L[c][r])

        synergy = abs(synergy1 - synergy2)

        if synergy < res:
            res = synergy

    print('#%d %d' % (tc, res))