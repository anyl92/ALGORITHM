# # summer/winter coding(~2018) 스킬트리
# def solution(skill, skill_trees):
#     answer = 0
#     for sk in skill_trees:
#         i = 0
#         for k in sk:
#             if k in skill:
#                 if i != skill.index(k):
#                     break
#                 i += 1
#         else:
#             print('sk', sk)
#             answer += 1
#     return answer
#
# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


# # 1
# def solution(p):
#     p += 1
#     while len(set(str(p))) != 4:
#         p += 1
#     return p
#
# solution(2015)


# # 2
# def solution(n):
#     answer = 0
#     return answer


# 3
def solution(total_sp, skills):
    answer = []
    N = len(skills) + 1
    indgree = [[] for _ in range(N+1)]
    num_indgree = [0 for _ in range(N+1)]

    for skill in skills:
        indgree[skill[0]].append(skill[1])
    for i, indg in enumerate(indgree):
        if i != 0 and not indg:
            num_indgree[i] = 1
    print(indgree, 'indg_first')
    print(num_indgree, 'num_first')

    result = [[] for _ in range(N)]
    chk_list = [0 for _ in range(N+1)]
    k = 0
    while sum(chk_list) != N:
        for i, indg in enumerate(indgree):
            if not chk_list[i]:
                for j in indg:
                    num_indgree[i] += num_indgree[j]
                    chk_list[j] = 1
        print('체크', num_indgree)
        print(chk_list, 'chk')

        # for num in num_indgree:
        #     if num:
        #         for i, indg in enumerate(indgree):
        #             if num in indg:
        #                 chk_list[i] = 1
        #                 num_indgree += 1
        # print(chk_list, 'chk')


    #         for i, indg in enumerate(indgree):
    #             if indg and pop_num in indg:
    #                 indg.remove(pop_num)
    #         result[k].append(pop_num)
    #     print(indgree)
    #     k += 1
    # print('결과', result)
    # for j in chk_list:
    #     if j and not chk_list[j]:
    #         boss_skill = j
    # print(boss_skill)
    # for res in result:
    #     pass
    return answer

solution(121, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]])
# def solution(total_sp, skills):
#     answer = []
#     N = len(skills) + 1
#     # up_skill = [0 for _ in range(N+1)]
#     indgree = [[] for _ in range(N+1)]
#
#     for skill in skills:
#         # up_skill[skill[0]] = 1
#         indgree[skill[0]].append(skill[1])
#     # print(up_skill)
#     print(indgree, 'firstt')
#
#     new_result = [0 for _ in range(N + 1)]
#     for i, indg in enumerate(indgree):
#         if not indg:
#             new_result[i] = 1
#     result = [[] for _ in range(N)]
#     chk_list = [0 for _ in range(N+1)]
#     k = 0
#     while sum(sum(indgree, [])) != 0:
#         pop_list = []
#         for i, indg in enumerate(indgree):
#             if i != 0 and chk_list[i] == 0 and not indg:
#                 pop_list.append(i)
#                 chk_list[i] = new_result[i]
#         print('팝리', pop_list)
#         print('체크', chk_list)
#
#         for pop_num in pop_list:
#             for i, indg in enumerate(indgree):
#                 if indg and pop_num in indg:
#                     indg.remove(pop_num)
#                     new_result[i] += 1
#             result[k].append(pop_num)
#         print(indgree)
#         print('ㄱㄱ', new_result)
#         k += 1
#     print('결과', result)
#     for j in chk_list:
#         if j and not chk_list[j]:
#             boss_skill = j
#     print(boss_skill)
#     for res in result:
#         pass
#     return answer


