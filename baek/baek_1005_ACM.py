import sys
sys.stdin = open('1005.txt', 'r')

for _ in range(int(input())):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    D.insert(0, 0)
    L = [list(map(int, input().split())) for _ in range(K)]
    W = int(input())
    print(N, K, D, W)
    print('ㅣ', L)

    preList = [[] for _ in range(K + 1)]
    # nextList = [[] for _ in range(K + 1)]
    visited = [0 for _ in range(K + 1)]

    for l in L:
        preList[l[1]].append(l[0])  # 선행되어야 하는 번호
        # nextList[l[0]].append(l[1])  # 다음 갈수있는 번호
    print(preList)

    time = D[W]
    q = preList[W]
    print(time, q)

    def sol(start, time):
        visited[start] = 1
