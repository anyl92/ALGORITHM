# # 1
# def solution(n):
#     answer = 0
#
#     five_calc = 5
#
#     while five_calc <= n:
#         answer += n // five_calc
#         five_calc *= 5
#
#     return answer
#
# print(solution(5))
# print(solution(10))


# # 2
# def solution(s):
#     answer = 0
#     answer_dict = {}
#
#     string_len = len(s)
#     for s_index in range(string_len):
#         string_part = ""
#         counting_letter = [0] * 26
#
#         for k in range(string_len - s_index):
#             letter_num = ord(s[s_index + k]) - 97
#             if counting_letter[letter_num]:
#                 break
#             else:
#                 counting_letter[letter_num] = 1
#
#             string_part += s[s_index + k]
#             if answer_dict.get(string_part):
#                 continue
#             else:
#                 answer_dict[string_part] = 1
#                 answer += 1
#
#     return answer
#
#
# print(solution("abac"))
# print(solution("abcd"))
# print(solution("zxzxz"))

# n = 1
# m = 26
# res = 0
# while m > 0:
#     res += (n*m)
#     n += 1
#     m -= 1
# print(res)


# 3
import heapq

def solution(N, coffee_times):
    answer = []
    coffee_heap = []

    idx = 0
    M = len(coffee_times)
    N = min(N, M)
    while idx < N:
        heapq.heappush(coffee_heap, (coffee_times[idx], idx))
        idx += 1

    while coffee_heap:
        cur_coffee = heapq.heappop(coffee_heap)
        time = cur_coffee[0]
        answer.append(cur_coffee[1] + 1)

        if idx < M:
            heapq.heappush(coffee_heap, (coffee_times[idx] + time, idx))
            idx += 1

    return answer


print(solution(3, [4, 2, 2, 5, 3]))
print(solution(1, [100, 1, 50, 1, 1]))

