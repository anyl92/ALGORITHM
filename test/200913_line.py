# 1
# def solution(boxes):
#     cnt = len(boxes)
#     new_boxes = [0 for _ in range(1001)]
#     for box in boxes:
#         if box[0] != box[1]:
#             # new_boxes += [box]
#             new_boxes[box[0]] += 1
#             new_boxes[box[1]] += 1
#
#             if new_boxes[box[0]] == 2:
#                 new_boxes[box[0]] = 0
#                 cnt -= 1
#             if new_boxes[box[1]] == 2:
#                 new_boxes[box[1]] = 0
#                 cnt -= 1
#         else:
#             cnt -= 1
#
#     return cnt
#
#
# print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))


# 2
# def solution(ball, order):
#     answer = []
#     tmp_list = []
#
#     for x in order:
#         # print(x, answer, tmp_list, ball, order)
#         if ball[0] == x:
#             answer.append(ball.pop(0))
#         elif ball[-1] == x:
#             answer.append(ball.pop())
#         else:
#             tmp_list.append(x)
#             # print(x, answer, tmp_list, ball, order)
#             continue
#
#         # print(x, answer, tmp_list, ball, order)
#
#         while tmp_list and ball:
#             if ball[0] in tmp_list:
#                 answer.append(ball.pop(0))
#                 continue
#             elif ball[-1] in tmp_list:
#                 answer.append(ball.pop())
#                 continue
#             else:
#                 break
#
#     # print(x, answer, tmp_list, ball, order)
#
#     return answer
#
#
# print(solution([11, 2, 9, 13, 24],	[9, 2, 13, 24, 11]))


# 3
def solution(n):
    str_n = str(n)
    ans_list = []

    def rec(s, cnt):
        len_s = len(s)
        for i in range(1, len_s):
            left, right = s[:i], s[i:len_s]
            if right[0] == '0':
                continue

            new_n = int(left) + int(right)
            if new_n < 10:
                ans_list.append([new_n, cnt + 1])
                return
            rec(str(new_n), cnt + 1)

    if len(str_n) < 2:
        return [0, n]
    rec(str_n, 0)

    tmp = 30
    answer = []
    for ans in ans_list:
        if tmp > ans[1]:
            tmp = ans[1]
            answer = [ans[1], ans[0]]

    return answer


# print(solution(10007))


# 4
def solution(maze):
    for m in maze:
        m.insert(0, 1)
        m.append(1)
    maze.insert(0, [1 for _ in range(len(maze[0]))])
    maze.append([1 for _ in range(len(maze[0]))])

    delta = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    answer = 0

    y, x, dir = 1, 1, 3
    while y != len(maze) - 2 or x != len(maze) - 2:
        dir = (dir + 3) % 4
        for i in range(4):
            ny = y + delta[(dir + i) % 4][0]
            nx = x + delta[(dir + i) % 4][1]
            if maze[ny][nx] == 0:
                y, x = ny, nx
                dir = (dir + i) % 4
                answer += 1
                break

    return answer


# print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))


# 5
def solution(companies, applicants):
    answer = []
    return answer


print(solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]))

# # 6
#
#
# print(solution())
