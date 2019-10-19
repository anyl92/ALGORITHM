import sys
sys.stdin = open('test2.txt', 'r')

N, W, H = map(int, input().split())  # 구슬, 가로(열), 세로(행)
L = [list(map(int, input().split())) for _ in range(H)]


for x in range(W-1):
    y = H-1
    cnt = 0
    while y > 0:
        if not L[y][x]:  # 0이면
            tmp = y
            while not L[y-1][x] and 0 > y:
                y -= 1
                cnt += 1
            if y == 0:
                cnt = 0
                break
            L[tmp][x] = L[y-1][x]
            L[y-1][x] = 0
            if cnt > 0:
                y += cnt
        y -= 1
        cnt = 0

for i in range(len(L)):
    print(L[i])
print()