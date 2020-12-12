# 1
def solution(S, K):
    day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i, day in enumerate(day_list):
        if day == S:
            i += K
            i %= 7
            return day_list[i]


# print(solution('Sat', 23))

# 2
def solution(N):
    num_list = list(str(N))
    leng = len(num_list)
    res_list = []

    flag = 0
    if num_list[0] == '-':
        num_list = num_list[1:]
        flag = 1

    for i in range(leng):
        num_list.insert(i, '5')
        res = ''
        for num in num_list:
            res += num
        res_list.append(res)
        num_list.pop(i)

    if flag:  # 음수
        L = [-1*x for x in list(map(int, res_list))]
        return max(L)
    else:
        return max(list(map(int, res_list)))


# print(solution(-54))

# 3
def solution(S, C):
    leng = len(S)
    res = 0
    j = 0
    for i in range(leng-1):
        if S[j] == S[i+1]:
            if C[j] <= C[i+1]:  # i+1이 더 크거나 같으면 i 더한다
                res += C[j]
                j = i + 1
            else:
                res += C[i+1]
        else:
            j = i + 1
        print(i, j, res)
    return res


# print(solution('aaaa', [3, 4, 5, 6]))
# print(solution('ababa', [10, 5, 10, 5, 10]))
# print(solution('aabbcc', [1, 2, 1, 2, 1, 2]))
# print(solution('abccbd', [0, 1, 2, 3, 4, 5]))
print(solution('aaaabb', [5, 1, 3, 0, 2, 2]))