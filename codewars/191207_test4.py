import copy

def solution(A):
    copyA = copy.deepcopy(A)
    mini = 99999
    for i in range(len(A)):
        cnt = 0
        tmp = A.pop(i)
        for num in A:
            if num == tmp:
                continue
            elif num + tmp == 7:
                cnt += 2
            else:
                cnt += 1
        if cnt < mini:
            mini = cnt
        A = copy.deepcopy(copyA)

    return mini


solution([1, 1, 6])