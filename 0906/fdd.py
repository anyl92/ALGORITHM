import sys
sys.stdin = open('input.txt', 'r')

def dfs(start):
    q = [start]
    visited = [0] * (V + 1)
    visited[start] = 1
    global count
    while q:
        count += 1
        for _ in range(len(q)):
            a = q.pop(0)
            for i in L:
                if i[0] == a and visited[i[1]]==0:
                    if i[1] == G[1]:
                        return count
                    visited[i[1]] = 1
                    q.append(i[1])
                elif i[1] == a and visited[i[0]]==0:
                    if i[0] == G[0]:
                        return count
                    visited[i[0]] = 1
                    q.append(i[0])
    count = 0
    if count == 0:
        return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(E)]
    G = list(map(int, input().split()))
    count = 0

    print('#%d %d' % (tc, dfs(G[0])))
