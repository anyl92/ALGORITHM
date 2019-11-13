import sys
sys.stdin = open('14501.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
maxi = 0

powerset = [[]]
for e in [i for i in range(N)]:
    powerset += [x + [e] for x in powerset]
powerset.pop(0)
print(powerset)

def aa():
    for pws in powerset:
        day = pws[0] + 1 + L[pws[0]][0]
        cost = L[pws[0]][1]

        if len(pws) <= 1:
            if day + L[pws[0]][0] <= N:
                # return L[pws[0]][1]
                continue

        for p in range(1, len(pws)):
            if day <= L[pws[p]]+1:
                if day + L[pws[p]][0] <= N:
                    day += L[pws[p]][0]
                    cost += L[pws[p]][1]

aa()