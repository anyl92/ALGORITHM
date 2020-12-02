# 5
def solution(n):
    answer = 0
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # x, y
    board = [[0 for _ in range(n)] for _ in range(n)]

    board[0][0] = 1
    stack = [[0, 0]]
    d = 0
    num = 2
    while stack:
        x, y = stack.pop()
        dx, dy = delta[d][0] + x, delta[d][1] + y

        if not (0 <= dx < n and 0 <= dy < n) or board[dy][dx]:
            d += 1
            if d == n + 1:
                d = 0
            dx, dy = delta[d][0] + x, delta[d][1] + y

        if not board[dy][dx]:
            board[dy][dx] = num
            num += 1
            stack.append([dx, dy])

    i, j = 0, 0
    while i < n:
        answer += board[i][j]
        i += 1
        j += 1

    return answer


n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")


# 6
def solution(pos):
    answer = 0
    delta = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

    x = ord(pos[0]) - 65
    y = (int(pos[1]) - 8) * -1

    for dx, dy in delta:
        xx, yy = dx + x, dy + y
        if 0 <= xx < 8 and 0 <= yy < 8:
            answer += 1

    return answer


pos = "A7"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")


#