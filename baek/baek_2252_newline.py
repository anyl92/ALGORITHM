import sys
sys.stdin = open('2252.txt', 'r')

N, rep = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(rep)]
# print(L)

nextList = [[] for _ in range(N+1)]
indgree = [0 for _ in range(N+1)]

for l in L:
    nextList[l[0]].append(l[1])
    indgree[l[1]] += 1
# print(nextList)
# print(indgree)

q = []
for i in range(1, N+1):
    if not indgree[i]:
        q.append(i)
# print('q', q)

while q:
    cur = q.pop(0)
    print(cur, end=' ')
    for j in nextList[cur]:
        if indgree[j]:
            indgree[j] -= 1
            if not indgree[j]:
                q.append(j)
