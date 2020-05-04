import sys
sys.stdin = open('1238.txt', 'r')

for tc in range(1, 11):
    T, start = map(int, input().split())
    L = list(map(int, input().split()))

    perList = [[] for _ in range(101)]
    visited = [0 for _ in range(101)]

    def personQ(s, cnt):
        q = [s]
        print(q, ',q')
        visited[s] = cnt
        while q:
            for _ in range(len(q)):
                cur = q.pop(0)
                for val in perList[cur]:
                    if visited[val] == 0:
                        visited[val] = cnt
                        q.append(val)
            cnt += 1

    for l in range(len(L)):
        if l % 2 == 0:
            perList[L[l]].append(L[l+1])

    personQ(start, 1)
    maxx = max(visited)
    for i, v in enumerate(visited):
        if v == maxx:
            result = i

    print('#%d %d' % (tc, result))