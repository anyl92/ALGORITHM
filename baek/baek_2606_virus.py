import sys
sys.stdin = open('2606.txt', 'r')

N = int(input())
M = int(input())
G = []
for _ in range(M):
    O, P = map(int, input().split())
    G.append(O)
    G.append(P)

L = [[] for _ in range(N+1)]
for i in range(len(G)//2):
    L[G[i*2]].append(G[i*2+1])
    L[G[i*2+1]].append(G[i*2])


def dfs(start):
    v = []
    s = [start]

    while s:
        n = s.pop()
        if n not in v:
            v.append(n)
            s.extend(L[n])
    return print(len(v)-1)

dfs(1)