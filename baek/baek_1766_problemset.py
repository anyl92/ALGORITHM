import sys
sys.stdin = open('1766.txt', 'r')

import heapq

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(M)]

q = []
v = [[] for _ in range(N+1)]
indg = [0] * (N+1)


def precalc(L):
    for f, b in L:
        indg[b] += 1  # indg 0인걸 먼저 보게하고
        v[f].append(b)  # visit에 다음 봐야할 수를 어펜드

    for i in range(1, N+1):
        if not indg[i]:
            heapq.heappush(q, i)
    return q


def sol(q):
    res = []
    while q:
        cur = heapq.heappop(q)
        res.append(cur)  # 먼저 보니까 res에 어펜드
        for i in v[cur]:
            indg[i] -= 1  # 내 다음 봐야할 애들을 indg에서 뺀다
            if not indg[i]:
                heapq.heappush(q, i)
    return res


for i in sol(precalc(L)):
    print(i, end=' ')