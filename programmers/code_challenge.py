# # 1
# def solution(numbers):
#     ans = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             k = numbers[i] + numbers[j]
#             ans.append(k)
#     return sorted(set(ans))
#
#
# print(solution([2,1,3,4,1]))

# # 2
# def solution(n):
#     answer = [[0]*x for x in range(1, n+1)]
#     cnt = sum(range(1, n+1)) - 1
#
#     dir = [(0, 1), (1, 0), (-1, -1)]
#     inp = 2
#     x, y = 0, 0
#     answer[y][x] = 1
#     code, i = 0, 1
#
#     while cnt:
#         xx, yy = dir[code][0] + x, dir[code][1] + y
#
#         if xx < 0 or xx >= n or yy < 0 or yy >= n:
#             code += 1
#             if code > 2:
#                 code %= 3
#             continue
#
#         if answer[yy][xx]:
#             code += 1
#             if code > 2:
#                 code %= 3
#             continue
#
#         answer[yy][xx] = inp
#         x, y = xx, yy
#         inp += 1
#         cnt -= 1
#     return sum(answer, [])
#
#
# print(solution(4))

# 3
from collections import deque

def solution(balloons):
    balloons_deq = deque()
    [balloons_deq.append(x) for x in balloons]

    bal = len(balloons_deq)
    if bal <= 2:
        return bal

    answer = 2
    pre = balloons_deq.popleft()
    cur = balloons_deq.popleft()
    bal = len(balloons_deq)

    # min_balloons = deque()
    # [min_balloons.append(x) for x in balloons_deq]
    min_balloons = [0 for _ in range(bal)]
    min_balloons[-1] = balloons_deq[-1]

    for x in range(bal-1, 0, -1):
        # if min_balloons[x] < min_balloons[x-1]:
        #     min_balloons[x-1] = min_balloons[x]
        if min_balloons[x] < balloons_deq[x-1]:
            min_balloons[x-1] = min_balloons[x]
        else:
            min_balloons[x-1] = balloons_deq[x-1]

    a, b = 0, 0
    while b < bal:
        # post = min_balloons.popleft()
        post = min_balloons[b]
        b += 1

        if pre < cur and post < cur:
            pass
        else:
            answer += 1

        if pre > cur:
            pre = cur
        # cur = balloons_deq.popleft()
        cur = balloons_deq[a]
        a += 1
    return answer


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))