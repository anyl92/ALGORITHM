import sys, collections
sys.stdin = open('1260.txt', 'r')

dfs_vst = collections.deque([])
def dfs(stp):
    dfs_vst.append(stp)
    for i in linked[stp]:
        if i not in dfs_vst:
            dfs(i)
    return


def bfs(stp):
    dq = collections.deque([stp])
    vst = collections.deque([])
    vst.append(stp)

    while dq:
        for _ in range(len(dq)):
            current = dq.popleft()
            for i in linked[current]:
                if i not in vst:
                    dq.append(i)
                    vst.append(i)
    return vst


N, M, V = map(int, input().split())
L = []
for _ in range(M):
    L += map(int, input().split())

linked = [[] for _ in range(N+1)]
for i in range(len(L)//2):
    linked[L[2*i]].append(L[2*i+1])
    linked[L[2*i+1]].append(L[2*i])

for i in linked:
    i.sort()

dfs_vst = collections.deque([])
dfs(V)
for j in dfs_vst:
    print(j, end=' ')

print()

vst = bfs(V)
for j in vst:
    print(j, end=' ')
