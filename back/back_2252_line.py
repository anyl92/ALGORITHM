import sys
sys.stdin = open('2252.txt', 'r')

N, rep = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(rep)]
# print(N, rep, L)

q = []
v = [0] * 100000
indg = [0] * 100000


def precalc(L):
    for line in L:
        f, b = line[0], line[1]
        indg[b] += 1
        
    for i in range(1, N+1):
        if not indg[i]:
            q.append(i)
    return q
    

def solution(q):
    res = []
    while q:
        cur = q.pop()
        res.append(cur)
        for i in range(v[cur]):
            indg[i] -= 1
            if not indg[i]:
                q.append(i)
    return res


print(solution(precalc(L)))