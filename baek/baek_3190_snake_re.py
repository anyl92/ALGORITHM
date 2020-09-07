import sys
sys.stdin = open('3190.txt', 'r')

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = 1

K = int(input())
for _ in range(K):
    apple = list(map(int, input().split()))
    board[apple[0]-1][apple[1]-1] = 4

L = int(input())
snake_dir = [list(input().split()) for _ in range(L)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

time = 0
cur_dir = 3
i, j = 0, 0
snake = [[0, 0]]

while True:
    time += 1
    ii, jj = dir[cur_dir]
    if 0 <= i+ii < N and 0 <= j+jj < N:
        ii, jj = i+ii, j+jj

        if board[ii][jj] == 1:
            print(time)
            break

        elif board[ii][jj] != 4:
            i, j = snake.pop(0)
            board[i][j] = 0

        board[ii][jj] = 1
        snake.append([ii, jj])
        i, j = ii, jj

    else:
        print(time)
        break

    if snake_dir and time == int(snake_dir[0][0]):
        _, tmp = snake_dir.pop(0)
        if tmp == 'L':
            if cur_dir == 0:
                cur_dir = 2
            elif cur_dir == 1:
                cur_dir = 3
            elif cur_dir == 2:
                cur_dir = 1
            else:
                cur_dir = 0
        else:
            if cur_dir == 0:
                cur_dir = 3
            elif cur_dir == 1:
                cur_dir = 2
            elif cur_dir == 2:
                cur_dir = 0
            else:
                cur_dir = 1
