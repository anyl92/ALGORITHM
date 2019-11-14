import sys
sys.stdin = open('1953.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    R, C, MR, MC, TI = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(R)]
    # (r, c)
    dir = [[(1, 0), (-1, 0), (0, 1), (0, -1)], [(1, 0), (-1, 0)], [(0, 1), (0, -1)],
           [(-1, 0), (0, 1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]]
    chk = [(1, 2, 4, 7), (1, 2, 5, 6), (1, 3, 6, 7), (1, 3, 4, 5)]

    def bfs(i, j):
        cnt = 0
        q = [(i, j)]
        vst = [[0 for _ in range(C)] for _ in range(R)]
        vst[i][j] = 1

        while q:
            for _ in range(len(q)):
                i, j = q.pop(0)
                for d in dir[L[i][j]-1]:
                    ii, jj = i+d[0], j+d[1]
                    if 0 <= ii < R and 0 <= jj < C and not vst[ii][jj]:
                        if L[ii][jj]:
                            if L[ii][jj] in chk[dir[0].index(d)]:
                                q.append((ii, jj))
                                vst[ii][jj] = 1
            cnt += 1

            if cnt == TI-1:
                return sum(vst, []).count(1)
        return sum(vst, []).count(1)

    if TI > 1:
        print('#%d %d' % (tc, bfs(MR, MC)))
    else:
        print('#%d' % (tc), 1)
