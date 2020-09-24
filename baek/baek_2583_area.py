import sys
sys.stdin = open('2583.txt', 'r')

M, N, K = map(int, input().split())
location = [list(map(int, input().split())) for _ in range(K)]
cnt_list = []
# print(M, N, K, location)

delta = [[-1, 0], [1, 0], [0, 1], [0, -1]]
V = [[0 for _ in range(N)] for _ in range(M)]
board = [[0 for _ in range(N)] for _ in range(M)]
area_cnt = 0

for loca in location:
    area_cnt += 1
    # print(loca, '변경전')
    loca[1] = M - 1 - loca[1]
    loca[3] = M - 1 - loca[3]
    # print(loca, '변경후')

    q = [[loca[0], loca[1]]]
    board[loca[1]][loca[0]] = area_cnt

    while q:
        x, y = q.pop(0)
        for xx, yy in delta:
            xx += x
            yy = y - yy
            # print(xx, yy, loca, '조건 맞잖아?')
            # print(xx, loca[0] <= xx < loca[2])
            # print(yy, loca[3] < yy <= loca[1])
            if loca[0] <= xx < loca[2] and loca[3] < yy <= loca[1]:
                # print(xx, yy, '안들어와?')
                if board[yy][xx] != area_cnt:
                    board[yy][xx] = area_cnt
                    q.append([xx, yy])

        # for b in board:
        #     print(b)
        # print()


def dfs(x, y):
    s = [[x, y]]
    V[y][x] = 1
    cnt = 1

    while s:
        x, y = s.pop()
        for xx, yy in delta:
            xx += x
            yy += y
            if 0 <= xx < N and 0 <= yy < M:
                if board[yy][xx] == 0 and V[yy][xx] == 0:
                    cnt += 1
                    s.append([xx, yy])
                    V[yy][xx] = 1
    cnt_list.append(cnt)


for i in range(M-1, -1, -1):
    for j in range(N):
        if board[i][j] == 0 and V[i][j] == 0:
            dfs(j, i)
            # area_cnt += 1

print(len(cnt_list))
for res in sorted(cnt_list):
    print(res, end=' ')