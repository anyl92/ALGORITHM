# # 1
# def solution(n):
#     answer = 0
#
#     three_list = []
#     while n > 0:
#         three_list.insert(0, n % 3)
#         n = n // 3
#
#     for i, num in enumerate(three_list):
#         answer += (3 ** i) * num
#
#     return answer
#
#
# print(solution(125))


# 4
def solution(s):
    answer = 0
    s_list = list(s)
    sub_list = []
    for i in range(len(s_list)+1):
        for j in range(i+1, len(s_list)+1):
            sub_list.append(s_list[i:j])

    for p in sub_list:
        start = 0
        end = len(p) - 1
        cur = 0
        while end > 0 and start < len(p):
            if p[start] != p[end]:
                if end - start > cur:
                    cur = end - start
                start += 1
                end = len(p) - 1
                continue
            end -= 1
        answer += cur

    return answer


print(solution("oo"))
