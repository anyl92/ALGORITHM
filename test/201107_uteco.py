# 1
# def solution(grades, weights, threshold):
#     ans = 0
#     grade_list = {'A+': 10, 'A0': 9,
#                   'B+': 8, 'B0': 7,
#                   'C+': 6, 'C0': 5,
#                   'D+': 4, 'D0': 3, 'F': 0}
#     len_list = len(grades)
#     for i in range(len_list):
#         ans += grade_list.get(grades[i]) * weights[i]
#     ans -= threshold
#
#     return ans
#
#
# print(solution(["B+","A0","C+"], [6,7,8], 200))

# 2
# def solution(s, op):
#     answer = []
#     for i in range(1, len(s)):
#         front = int(s[:i])
#         back = int(s[i:])
#
#         if op == '+':
#             answer += [front + back]
#         elif op == '-':
#             answer += [front - back]
#         else:
#             answer += [front * back]
#     return answer
#
#
# print(solution("1234", "+"))

# 3
# def solution(money, expected, actual):
#     cur = 100
#     len_list = len(expected)
#
#     for i in range(len_list):
#         if money <= 0:
#             return 0
#         if expected[i] == actual[i]:
#             money += cur
#             cur = 100
#         else:
#             money -= cur
#             if cur * 2 > money:
#                 cur = money
#             else:
#                 cur *= 2
#     return money
#
#
# print(solution(1200, ["T", "T", "H", "H", "H"], ["H", "H", "T", "H", "T"]))

# 4
# def solution(n, board):
#     delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#     q = [[0, 0]]
#
#     def bfs(q, cnt_num, answer):
#         if cnt_num == n*n + 1:
#             return answer
#
#         v = [[0 for _ in range(n)] for _ in range(n)]
#
#         while q:
#             answer += 1
#             for _ in range(len(q)):
#                 i, j = q.pop(0)
#                 v[i][j] = 1
#
#                 for d in delta:
#                     ii = d[0] + i
#                     jj = d[1] + j
#                     if ii == -1: ii = n - 1
#                     elif ii == n: ii = 0
#                     if jj == -1: jj = n - 1
#                     elif jj == n: jj = 0
#                     if not v[ii][jj]:
#                         if board[ii][jj] == cnt_num:
#                             answer += 1  # 엔터
#                             return bfs([[ii, jj]], cnt_num+1, answer)
#                         q.append([ii, jj])
#                         v[ii][jj] = 1
#     return bfs(q, 1, 0)
#
#
# print(solution(2, [[2, 3], [4, 1]]))

# 5
# def solution(penter, pexit, pescape, data):
#     answer = ''
#     penter_len = len(penter)
#     result_list = [penter]
#
#     for i in range(0, len(data), penter_len):
#         data_piece = ''
#         for j in range(penter_len):
#             data_piece += data[i+j]
#
#         if data_piece == penter or data_piece == pexit or data_piece == pescape:
#             result_list += [pescape + data_piece]
#         else:
#             result_list += [data_piece]
#     result_list += [pexit]
#
#     for result in result_list:
#         answer += result
#     return answer
#
#
# print(solution("1100","0010","1001","1101100100101111001111000000"))

# 6
# def solution(logs):
#     answer = []
#     inp_dict = {}
#     for log in logs:
#         log = log.split()
#         if inp_dict.get(log[0]):
#             inp_dict[log[0]][0][log[1]] = log[2]
#         else:
#             inp_dict[log[0]] = [{log[1]: log[2]}]
#
#     key_list = []
#     for key in inp_dict.keys():
#         key_list += [key]
#
#     for k in range(len(key_list)-1):
#         if len(inp_dict[key_list[k]][0]) >= 5:
#             if inp_dict[key_list[k]][0] == inp_dict[key_list[k+1]][0]:
#                 answer += [key_list[k], key_list[k+1]]
#
#     new_answer = []
#     for ans in set(answer):
#         new_answer += [ans]
#
#     if not new_answer:
#         return ["None"]
#     return sorted(new_answer)
#
#
# print(solution(["1901 10 50", "1909 10 50"]))

# 7
def solution(n, horizontal):
    answer = [[0 for _ in range(n)] for _ in range(n)]

    if horizontal:
        flag = 1
    else:
        flag = 0
    flag_list = [[-1, 1], [1, -1]]  # 오른쪽위, 왼쪽아래

    right = [0, 1]
    down = [1, 0]
    delta = []
    for i in range(n-1):
        if horizontal:
            delta += [right]
        else:
            delta += [down]
        horizontal = not horizontal
    delta += delta[::-1]

    y, x, cnt = 0, 0, 0
    for yy, xx in delta:
        yy += y
        xx += x
        cnt += 1
        answer[yy][xx] = cnt

        yyy, xxx = yy, xx
        while True:
            if yyy == xx and xxx == yy:
                flag = not flag
                y = yyy
                x = xxx
                break
            i, j = flag_list[flag]
            yyy += i
            xxx += j
            if 0 <= yyy < n and 0 <= xxx < n:
                cnt += 2
                answer[yyy][xxx] = cnt

    return answer


print(solution(2, False))