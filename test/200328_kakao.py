# 1
def solution1(board, moves):
    stack = []
    answer = 0
    for move in moves:
        for y in range(len(board)):
            if board[y][move - 1]:
                stack.append(board[y][move - 1])
                board[y][move - 1] = 0
                break
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
    return answer


# 2
def solution2(s):
    answer = []

    return answer

# solution({{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}})
# input = {{1,2,3},{2,1},{1,2,4,3},{2}}
blank = []

# for l in {{1,2,3},{2,1},{1,2,4,3},{2}}:
#     blank[len(l)] = l
print(blank)
print()
# for l in li:
#     len(l)


# 3
def solution3(user_id, banned_id):
    answer = 0
    ban_list = []
    for ban in banned_id:
        chk_user = []
        for user in user_id:
            if len(ban) == len(user):
                chk_user.append(user)
        for banidx in range(len(ban)):
            if ban[banidx] == '*':
                continue
            delli = []
            for user_idx, user in enumerate(chk_user):
                if user[banidx] != ban[banidx]:
                    delli.append(user_idx)
            print('유저목록,지울인덱스', chk_user, delli)
            for d in delli[::-1]:
                print('유저목록,지울인덱스,지울배열', chk_user, d, delli[:])
                chk_user.pop(d)
        ban_list.append(chk_user)
    for i in range(len(ban_list)-1):
        for j in range(i+1, len(ban_list)):
            if ban_list[i] == ban_list[j]:

    return print(ban_list)

solution3(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
