import sys
sys.stdin = open('15685.txt', 'r')

N = int(input())
L = [[0 for _ in range(101)] for _ in range(101)]

dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # x, y
dir_rule = [1, 2, 3, 0]  # 0, 1, 2, 3

def curve(x, y, d, G):
    # G 0일때
    L[y][x] = 1
    dir_list = [d]
    x, y = x + dir[d][0], y + dir[d][1]
    L[y][x] = 1
    if G == 0:
        return

    # G 1일때
    d = dir_rule[d]  # 0->1
    dir_list += [d]
    x, y = x + dir[d][0], y + dir[d][1]
    L[y][x] = 1
    if G == 1:
        return

    # G 2이상
    for _ in range(G-1):
        ld = len(dir_list)
        for i in range(ld):
            if ld//2 > i:
                if dir_list[i] < 2:
                    d = dir_list[i] + 2
                else:
                    d = dir_list[i] - 2
            else:
                d = dir_list[i]
            x, y = x + dir[d][0], y + dir[d][1]
            dir_list += [d]
            L[y][x] = 1


check_dir = [(1, 0), (0, 1), (1, 1)]
cnt = 0

def check(j, i):
    global cnt
    for d in check_dir:
        jj, ii = j + d[0], i + d[1]
        if 0 <= jj < 101 and 0 <= ii < 101:
            if not L[ii][jj]:
                return
    cnt += 1


for _ in range(N):
    x, y, d, G = map(int, input().split())
    curve(x, y, d, G)

for i in range(100):
    for j in range(100):
        if L[i][j]:
            check(j, i)

print(cnt)