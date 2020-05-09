import sys
sys.stdin = open('1267.txt', 'r')

for tc in range(1, 11):
    V, E = map(int, input().split())
    L = list(map(int, input().split()))
    print(V, E, L)

    rangeList = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    print(visited)

    for i in range(len(L)):
        if i % 2 == 0:
            rangeList[L[i]].append(L[i+1])
    print(rangeList)

