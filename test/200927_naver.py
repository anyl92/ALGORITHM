# # 1
# def solution(m, k):
#     answer = ''
#     input_list = list(m)
#     key_list = list(k)
#     for inp in input_list:
#         if key_list and inp == key_list[0]:
#             key_list.pop(0)
#             continue
#         answer += inp
#         # print(answer)
#     return answer
#
#
# solution("acbbcdc", "abc")


# def solution(blocks):
#     # answer = []
#     len_blocks = len(blocks)
#     res_list = [[False] * i for i in range(1, len_blocks+1)]
#     print(res_list)
#
#     for idx, block in enumerate(blocks):
#         res_list[idx][block[0]] = block[1]
#     print(res_list)
#
#     for i in range(1, len_blocks):
#         for j in range(i+1):  # 0 1  23
#             if res_list[i][j]:
#                 k = j
#                 while k > 0:
#                     cur = res_list[i][k]
#                     pre = res_list[i][k - 1]
#                     if pre == False:
#                         res_list[i][k - 1] = res_list[i-1][k-1] - cur
#                     k -= 1
#
#                 k = j
#                 while k < i:
#                     cur = res_list[i][k]
#                     post = res_list[i][k+1]
#                     if post == False:
#                         res_list[i][k+1] = res_list[i-1][k] - cur
#                     k += 1
#                 break
#     print(res_list)
#     answer = sum(res_list, [])
#     print(answer)
#     return answer
#
#
# solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]])


childs = [0 for _ in range(50)]


def preorder(L, n):
    cnt = 0
    for i in range(len(L[n])):
        # print(L[n][i])
        # print(cnt)
        cnt += preorder(L, L[n][i])
        cnt += 1
    childs[n] = cnt
    return cnt


def dfs(i, cnt):



def solution(n, edges):
    answer = 0
    L = [[] for _ in range(n)]
    for edge in edges:
        L[edge[0]] += [edge[1]]
    print(L)

    level = [[] for _ in range(50)]
    level[0] = [0]
    level[1] += L[0]

    q = [i for i in L[0]]
    k = 2
    while q:
        for _ in range(len(q)):
            cur = q.pop(0)
            level[k] += L[cur]
            q.extend(L[cur])
        k += 1
    print(k-1, level)

    depth = k-1
    preorder(L, 0)
    print(childs)

    dfs(0, 0)

    return answer


solution(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]])