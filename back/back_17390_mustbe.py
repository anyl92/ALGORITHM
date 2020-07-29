import sys
sys.stdin = open('17390.txt', 'r')

N, Q = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
questions = [list(map(int, input().split())) for _ in range(Q)]

for i in range(1, N):
    numbers[i] = numbers[i] + numbers[i-1]

for l, r in questions:
    if l == 1:
        print(numbers[r-1])
    else:
        print(numbers[r-1] - numbers[l-2])


# def merge(left, right):
#     i, j = 0, 0
#     sorted_list = []
#
#     while (i < len(left)) & (j < len(right)):
#         if left[i] < right[j]:
#             sorted_list.append(left[i])
#             i += 1
#         else:
#             sorted_list.append(right[j])
#             j += 1
#
#     while i < len(left):
#         sorted_list.append(left[i])
#         i += 1
#
#     while j < len(right):
#         sorted_list.append(right[j])
#         j += 1
#
#     return sorted_list
#
#
# def merge_sort(unsorted_list):
#     if len(unsorted_list) <= 1:
#         return unsorted_list
#
#     mid = len(unsorted_list) // 2
#     left = unsorted_list[:mid]
#     right = unsorted_list[mid:]
#
#     left1 = merge_sort(left)
#     right1 = merge_sort(right)
#
#     return merge(left1, right1)
#
#
# def pre_calc(L):
#     i = 1
#     while i < N:
#         for j in range(N-i):
#             tmp = 0
#             for k in range(i+1):
#                 tmp += L[j+k]
#             pre_calc_list[i].append(tmp)
#         i += 1
#
#
# N, Q = map(int, input().split())
# numbers = list(map(int, input().split()))
# questions = [list(map(int, input().split())) for _ in range(Q)]
# # print(N, Q, numbers, questions)
#
# sorted_numbers = merge_sort(numbers)
# pre_calc_list = [[] for _ in range(N)]
# pre_calc_list[0] = sorted_numbers
# pre_calc(sorted_numbers)
# # print(sorted_numbers, pre_calc_list)
#
# for q in questions:
#     find_idx = q[1] - q[0]
#     find_sum = q[0] - 1
#     print(pre_calc_list[find_idx][find_sum])
