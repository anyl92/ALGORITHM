import sys
sys.stdin = open('1012.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    R, C, K = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(K)]

    mat = [[0]*(R) for _ in range(C)]

    for l in L:
        mat[l[1]][l[0]] = 1
    
    for z in mat:
        print(z)

    v = [[0]*(R) for _ in range(C)]
    def dfs(r, c):
        s = [(r, c)]
        v[c][r] = 1

        while s:
            x, y = s.pop()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                xx, yy = x+dx, y+dy
                if 0 <= xx < R and 0 <= yy < C:
                    if v[yy][xx] == 0 and mat[yy][xx]:
                        v[yy][xx] = 1
                        s.append((xx, yy))

    cnt = 0
    for r in range(R):
        for c in range(C):
            if mat[c][r] and v[c][r] == 0:
                dfs(r, c)
                cnt += 1
            
    print(cnt)