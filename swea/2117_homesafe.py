import sys
sys.stdin = open('2117.txt', 'r')


def find(q, k):
    i, j = q[0], q[1]
    vst = [[0 for _ in range(N)] for _ in range(N)]
    vst[i][j] = 1
    q = [q]
    if L[i][j]:
        home = 1
    else:
        home = 0

    while k > 1:
        for _ in range(len(q)):
            i, j = q.pop(0)
            for d in dir:
                ii, jj = i + d[0], j + d[1]
                if 0 <= ii < N and 0 <= jj < N and not vst[ii][jj]:
                    if L[ii][jj]:
                        home += 1
                    q.append([ii, jj])
                    vst[ii][jj] = 1
        k -= 1

    bene = (home * M) - cost
    if bene >= 0:
        return home
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    res = 0
    k = 0

    for n in range(1, 2*N+2):
        if n % 2 == 1:
            k += 1
            cost = k * k + (k - 1) * (k - 1)

            for i in range(N):
                for j in range(N):
                    cnt = find([i, j], k)

                    if cnt > res:
                        res = cnt

    print('#%d %d' % (tc, res))