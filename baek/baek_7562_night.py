import sys
sys.stdin = open('7562.txt', 'r')

direc = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
T = int(input())
for tc in range(T):
    N = int(input())
    cx, cy = map(int, input().split())
    nx, ny = map(int, input().split())


    def bfs(cx, cy):
        q = [[cx, cy]]
        V = [[0 for _ in range(N)] for _ in range(N)]
        V[cy][cx] = 1
        cnt = 0

        while q:
            cnt += 1
            for _ in range(len(q)):
                cx, cy = q.pop(0)
                for dx, dy in direc:
                    xx, yy = cx + dx, cy + dy
                    if xx == nx and yy == ny:
                        return cnt
                    if 0 <= xx < N and 0 <= yy < N:
                        if not V[yy][xx]:
                            V[yy][xx] = 1
                            q.append([xx, yy])

    if cx == nx and cy == ny:
        print(0)
    else:
        print(bfs(cx, cy))