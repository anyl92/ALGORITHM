import itertools

def solution(A, B, C, D):
    numlist = [A, B, C, D]
    permlist = list(itertools.permutations(numlist, 4))
    timelist = []

    for perm in permlist:
        hour = ''
        minu = ''
        hour = str(perm[0]) + str(perm[1])
        minu = str(perm[2]) + str(perm[3])

        if int(hour) < 24 and int(minu) < 59:
            timelist += [hour+minu]

    return len(set(timelist))


print(solution(2, 3, 3, 2))