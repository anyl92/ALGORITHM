import sys
sys.stdin = open('2252.txt', 'r')

N, rep = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(rep)]

q = []
v = [[] for _ in range(N+1)]
indg = [0] * (N+1)


def precalc(L):
    for f, b in L:
        indg[b] += 1
        v[f].append(b)
        
    for i in range(1, N+1):
        if not indg[i]:
            q.append(i)
    return q
    

def solution(q):
    res = []
    while q:
        cur = q.pop()
        res.append(cur)
        for i in v[cur]:
            indg[i] -= 1
            if not indg[i]:
                q.append(i)
    return res


for i in solution(precalc(L)):
    print(i, end=' ')