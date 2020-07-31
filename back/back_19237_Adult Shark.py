import sys
sys.stdin = open('19237.txt', 'r')

N, M, k = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
d = list(map(int, input().split()))
print(N, M, k, d)
P = [[] for _ in range(M)]
for m in range(M):
    for _ in range(4):
        P[m] += [list(map(int, input().split()))]
print(P)

# 초기 배열
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
smell = [[() for _ in range(N)] for _ in range(N)]
move = [[() for _ in range(N)] for _ in range(N)]
time = 1
for i in range(N):
    for j in range(N):
        if L[i][j]:
            cur = L[i][j]
            smell[i][j] = cur, k
            move[i][j] = cur, d[cur-1]

# 이동하기
for i in range(N):
    for j in range(N):
        if move[i][j]:
            print(move[i][j])
            cur_n = move[i][j][0]
            cur_d = move[i][j][1]
            cur_p = P[cur_n - 1][cur_d - 1]
            # 보고있는 방향에 따라 이동할 위치방향 바꿔주기
            if cur_d == 1:  # 위 1234->4312
                for a in range(4):
                    if cur_p[a] == 1: cur_p[a] = 4
                    elif cur_p[a] == 2: cur_p[a] = 3
                    elif cur_p[a] == 3: cur_p[a] = 1
                    else: cur_p[a] = 2
            elif cur_d == 2:  # 아래 1234->3421
                for a in range(4):
                    if cur_p[a] == 1: cur_p[a] = 3
                    elif cur_p[a] == 2: cur_p[a] = 4
                    elif cur_p[a] == 3: cur_p[a] = 2
                    else: cur_p[a] = 1

            for p in cur_p:
                idx, jdx = dir[p-1]
                if 0 <= i+idx < N and 0 <= j+jdx < N:
                    move[i+idx][j+jdx] = move[i][j]
                    # 옮길 수 있으면 옮기고 포문 나가기
                # 안되면 다음 방향

# 배열 하나로 다시 고치기