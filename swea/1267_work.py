import sys
sys.stdin = open('1267.txt', 'r')

for tc in range(1, 11):
    V, E = map(int, input().split())
    L = list(map(int, input().split()))
    # print(V, E, L)

    nextList = [[] for _ in range(V+1)]  # 내 자리에서 다음으로 가는 리스트를 입력
    # chkList = [[] for _ in range(V+1)]
    # visited = [0 for _ in range(V+1)]
    indgree = [0 for _ in range(V+1)]

    for i in range(len(L)):
        if i % 2 == 0:
            nextList[L[i]].append(L[i + 1])
        elif i % 2:
            indgree[L[i]] += 1
    # print('next', nextList)
    # print('indg', indgree)

    q = []
    for j in range(1, V+1):
        if not indgree[j]:
            q.append(j)
    # print('q', q)

    result = []
    while q:
        cur = q.pop(0)
        result.append(cur)
        for k in nextList[cur]:
            if indgree[k]:
                indgree[k] -= 1
                if not indgree[k]:
                    q.append(k)


    print('#%d' % (tc), end=' ')
    for r in result:
        print(r, end=' ')
    print()