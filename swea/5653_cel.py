import sys
sys.stdin = open('5653.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 하상우좌
    vst = [[0 for _ in range(M + K)] for _ in range(N + K)]

    L = [[0 for _ in range(M + K)] for _ in range(N + K)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                L[(K//2)+i][(K//2)+j] = [arr[i][j], 0]

    # CL = [[0 for _ in range(M + K)] for _ in range(N + K)]
    cnt = 0


    def bfs(r, c):
        global cnt

        q = [(r, c)]
        vst[r][c] = 1

        for d in dir:
            rr, cc = r+d[0], c+d[1]
            if 0 <= rr < N+K and 0 <= cc < M+K:
                if not L[rr][cc] and not vst[rr][cc]:
                    q.append((rr, cc))
                    vst[rr][cc] = 1
                    L[rr][cc] = [L[r][c][0], -1]


    k = 0
    while k < K:
        for i in range(N + K):
            for j in range(M + K):
                if L[i][j]:
                    L[i][j][1] += 1  # 1시간 후
                if L[i][j] and L[i][j][0] * 2 == L[i][j][1]:  # 죽음
                    L[i][j][0] = 0

        bfs_list = [[] for _ in range(10)]
        for i in range(N + K):
            for j in range(M + K):
                if L[i][j] and L[i][j][0] == L[i][j][1]:  # 활성
                    bfs_list[L[i][j][0]-1] += [(i, j)]
        # print(bfs_list)

        # for l in L:
        #     print(l)
        # print()

        for b in bfs_list:
            for i, j in b:
                bfs(i, j)

        k += 1

    for i in range(N + K):
        for j in range(M + K):
            if L[i][j] and L[i][j][0] * 2 == L[i][j][1]:  # 죽음
                L[i][j][0] = 0
            if L[i][j] and L[i][j][0]:
                cnt += 1

    for l in L:
        print(l)
    print()

    print('#%d %d' % (tc, cnt))