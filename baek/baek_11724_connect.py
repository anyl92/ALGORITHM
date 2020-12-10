import sys
sys.stdin = open('11724.txt', 'r')

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(M)]


def dfs(n):
    V[n] = 1

    for nn in node[n]:
        if not V[nn]:
            dfs(nn)


node = [[] for _ in range(N+1)]
for l in L:
    node[l[0]] += [l[1]]
    node[l[1]] += [l[0]]

V = [0 for _ in range(N+1)]

ans = 0
for k in range(1, N+1):
    if not V[k]:
        dfs(k)
        ans += 1
print(ans)
