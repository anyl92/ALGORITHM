import sys
sys.stdin = open('14888.txt', 'r')

import itertools

N = int(input())
L = list(map(int, input().split()))
O = list(map(int, input().split()))

opr = []
for i in range(4):
    for j in range(O[i]):
        opr += [i]

perm = list(itertools.permutations(opr, N-1))

minn = 10000000000001
maxx = -10000000000001

for p in perm:
    tot = L[0]
    for i in range(1, N):
        if p[i-1] == 0:  # +
            tot += L[i]
        elif p[i-1] == 1:  # -
            tot -= L[i]
        elif p[i-1] == 2:  # *
            tot *= L[i]
        else:
            tot = int(tot / L[i])

    if tot < minn:
        minn = tot
    if tot > maxx:
        maxx = tot

print(maxx)
print(minn)