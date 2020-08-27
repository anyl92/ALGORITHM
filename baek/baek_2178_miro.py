import sys
sys.stdin = open('2178.txt', 'r')

N, M = map(int, input().split())
L = []
for i in range(N):
    tmp = list(input())
    L += [list(map(int, tmp))]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 좌, 우, 상, 하


def bfs(j, i):
    cnt = 1
    q = [(j, i)]
    vst = [[0]*M for _ in range(N)]
    vst[i][j] = 1

    while q:
        for _ in range(len(q)):
            cur = q.pop(0)
            for d in dir:
                xx = cur[0] + d[0]
                yy = cur[1] + d[1]
                if 0 <= xx < M and 0 <= yy < N:
                    if xx == M-1 and yy == N-1:
                        cnt += 1
                        return cnt
                    if vst[yy][xx] == 0 and L[yy][xx] == 1:
                        q.append((xx, yy))
                        vst[yy][xx] = 1
        cnt += 1


print(bfs(0, 0))