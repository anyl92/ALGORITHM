# 1
# def solution(a, b):
#     answer = 0
#     for i in range(len(a)):
#         answer += a[i] * b[i]
#     return answer
#
#
# print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))

# 2
# def solution(s):
#     zero_cnt = 0
#     cnt = 0
#     while True:
#         s_list = ''
#         s_len = len(s)
#
#         for i in s:
#             if i == '1':
#                 s_list += i
#                 s_len -= 1
#         zero_cnt += s_len
#         n = len(s_list)
#
#         r_list = ''
#         while n > 0:
#             r_list += str(n % 2)
#             n //= 2
#         cnt += 1
#         s = r_list
#
#         if r_list == '1':
#             answer = [cnt, zero_cnt]
#             break
#
#     return answer
#
#
# print(solution("1111111"))

# 3
def solution(a):
    answer = -1
    counting_list = [[0, []] for _ in range(len(a))]
    for i, e in enumerate(a):
        counting_list[e][0] += 1
        counting_list[e][1].append(i)
    print(counting_list)

    counting_list.sort()
    print(counting_list)

    std_num, std_idx = counting_list.pop()
    # for i, idx in enumerate(std_idx):
    for i in range(1, len(std_idx)):
        # print(idx,'악')
        a[i-1]

    answer_list = []
    tmp_list = []


    return answer


print(solution([5,2,3,3,5,3]))