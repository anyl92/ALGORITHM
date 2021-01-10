# 1
# def solution(lottos):
#     answer = ''
#     num_count = [0] * 50
#     bonus_num_count = [0] * 50
#     for lotto in lottos:
#         for lo in lotto.split():
#             if lo[0] == '(':
#                 lo = lo[1:]
#                 lo = lo[:-1]
#                 bonus_num_count[int(lo)] += 1
#             else:
#                 num_count[int(lo)] += 1
#
#     cnt = max(num_count)
#     correct_nums = []
#     k = 0
#     while k < 6:
#         for i, num in enumerate(num_count):
#             if num == cnt and i:
#                 correct_nums.append(i)
#                 k += 1
#             if k == 6:
#                 break
#         cnt -= 1
#     correct_nums = sorted(correct_nums)
#
#     bonus_cnt = max(bonus_num_count)
#     flag = 1
#     while flag:
#         for i, b_num in enumerate(bonus_num_count):
#             if b_num == bonus_cnt:
#                 if i in correct_nums:
#                     continue
#                 elif i:
#                     bonus_num = i
#                     flag = 0
#                     break
#         bonus_cnt -= 1
#
#     flag = 1
#     for key, val in enumerate(correct_nums):
#         if flag and val > bonus_num:
#             answer += '(' + str(bonus_num) + ')' + ' '
#             answer += str(val) + ' '
#             flag = 0
#         else:
#             answer += str(val) + ' '
#
#     return answer[:-1]
#
#
# print(solution(["15 10 39 5 1 21 (22)", "11 5 (10) 39 1 8 44", "(39) 10 5 22 15 9 20", "22 10 5 1 (15) 3 2", "10 (5) 22 1 15 41 38", "10 5 39 33 17 14 (1)"]))


# 3
# def solution(black_caps):
#     leng = len(black_caps)
#     answer = [0] * leng
#
#     answer[1] = 1 if black_caps[0] else 2
#     answer[-2] = 1 if black_caps[-1] else 2
#
#     for i in range(1, leng-1):
#         if not black_caps[i]:  # 0은 앞뒤 둘다 흰
#             answer[i-1] = 2
#             answer[i+1] = 2
#
#     for j in range(1, leng-1):
#         if black_caps[j] == 2:  # 2는 앞뒤 둘다 검
#             answer[j-1] = 1
#             answer[j+1] = 1
#
#     for k in range(1, leng-1):
#         if black_caps[k] == 1:  # 아직 알 수 없는 사람
#             # 둘 중 하나가 2면 다른애는 1
#             # 둘 중 하나가 1면 다른애가 2
#             # 둘 다 0이면 그대로
#
#             if answer[k-1] == 1:
#                 answer[k+1] = 2
#             elif answer[k-1] == 2:
#                 answer[k+1] = 1
#             elif answer[k+1] == 1:
#                 answer[k-1] = 2
#             elif answer[k+1] == 2:
#                 answer[k-1] = 1
#
#     for l in range(leng-2, 0, -1):
#         if black_caps[k] == 1:  # 바뀐 경우 대비 한번더 검증
#             if answer[k - 1] == 1:
#                 answer[k + 1] = 2
#             elif answer[k - 1] == 2:
#                 answer[k + 1] = 1
#             elif answer[k + 1] == 1:
#                 answer[k - 1] = 2
#             elif answer[k + 1] == 2:
#                 answer[k - 1] = 1
#
#     return answer
#
#
# print(solution([1, 1, 2, 0]))
# print(solution([1, 1, 1]))


# 2
def solution(links):
    answer = 0
    len_links = len(links)

    ceo = 0
    for i in range(1, len_links+2):
        ceo += i
    for link in links:
        ceo -= link[1]

    trees = [[] for _ in range(len_links+2)]
    for link in links:
        trees[link[0]] += [link[1]]

    def recur(cur):
        if trees[cur]:
            cur_o, cur_x = 1, 0
            for k in trees[cur]:
                o, x = recur(k)
                cur_o *= x
                cur_x += o

            len_e = len(trees[cur])
            y, tmp = 0, 1
            for i in range(len_e):
                tmp = 1
                for j in range(len_e):
                    if i != j:
                        tmp *= answer[trees[cur][j]][1]
                tmp *= answer[trees[cur][i]][0]
                y += tmp
            answer[cur] = [cur_o, y]

        return answer[cur]

    answer = [[1, 1] for _ in range(len_links + 2)]
    recur(ceo)
    result = sum(answer[ceo])

    return result

# print(solution([[4, 5], [4, 3], [4, 2], [1, 6], [7, 4], [7, 1]]))
print(solution([[3, 5], [3, 2], [6, 3], [6, 1], [4, 6]]))
