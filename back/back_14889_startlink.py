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


def perm(k):
    global start, link
    for i in range(k, N):
        if V[i] == 1:
            continue
        if (sorted(T[:N//2]) in start) or (sorted(T[N//2:]) in link):
            T[k], T[i] = T[i], T[k]
            V[i] = 1
            perm(k + 1)
            T[k], T[i] = T[i], T[k]
            V[i] = 0
        else:
            start += [sorted(T[:N // 2])]
            link += [sorted(T[N // 2:])]
            T[k], T[i] = T[i], T[k]
            V[i] = 1
            perm(k + 1)
            T[k], T[i] = T[i], T[k]
            V[i] = 0
            calc(T)


N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

start, link = [], []
V = [0] * N
T = [i for i in range(N)]
mini = 999999

perm(0)
print(mini)