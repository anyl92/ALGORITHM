import sys
sys.stdin = open('16724.txt', 'r')

R, C = map(int, input().split())
L = [list(input()) for _ in range(R)]
V = [[0 for _ in range(C)] for _ in range(R)]
turn_cnt = R*C


def move(i, j):
    move_cnt = 0
    V[i][j] = cnt

    y, x = i, j
    while move_cnt <= turn_cnt:
        char = L[y][x]  # 좌표 문자 방향대로 이동하기
        if char == 'U':
            y -= 1
        elif char == 'D':
            y += 1
        elif char == 'L':
            x -= 1
        elif char == 'R':
            x += 1

        if V[y][x] == V[i][j]:  # 들어온 자리에 다시 방문하면 설치 대상이므로 cnt증가
            return 1
        if V[y][x]:  # route 따라 돌다가 숫자면 여기 합류하므로 나가기
            return 0

        V[y][x] = cnt
        move_cnt += 1
    return 0


cnt, ans = 1, 0
for i in range(R):
    for j in range(C):
        if V[i][j]:
            continue
        else:
            ans += move(i, j)
            cnt += 1
print(ans)