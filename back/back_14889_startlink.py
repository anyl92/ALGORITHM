import sys
sys.stdin = open('input.txt', 'r')


def calc(T):
    global mini
    start = T[:N//2]
    link = T[N//2:]
    SA, LA = 0, 0

    for i in range(len(start)-1):
        for j in range(i+1, len(start)):
            SA += L[start[i]][start[j]]
            SA += L[start[j]][start[i]]
            LA += L[link[i]][link[j]]
            LA += L[link[j]][link[i]]
    tmp = abs(SA-LA)

    if mini > tmp:
        mini = tmp


def combinations(n, list, combos=[]):
    if combos is None:
        combos = []

    if len(list) == n:
        if combos.count(list) == 0:
            combos.append(list)
        return combos
    else:
        for i in range(len(list)):
            refined_list = list[:i] + list[i+1:]
            combos = combinations(n, refined_list, combos)
        return combos


N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

tr = [0] * 4
an = [0] * N
T = [i for i in range(N)]
mini = 999999

C = combinations(N//2, T)

tmp = []
for i in range(len(C)):
    for j in range(len(C)):
        if i != j:
            if len(set(C[i] + C[j])) == N:
                calc(C[i] + C[j])
                break
print(mini)