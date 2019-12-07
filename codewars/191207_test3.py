import itertools

def solution(S):
    ordlist = []
    for s in S:
        ordlist.append(ord(s))
    print(ordlist)

    ordcomblist = list(itertools.combinations(ordlist, len(ordlist)-1))
    print(ordcomblist)

    mini = 9999999
    chklist = []
    for ordcomb in ordcomblist:
        absval = 0
        for i in range(len(ordcomb)-1):
            absval += abs(ordcomb[i] - ordcomb[i+1])
        chklist += [(absval, sum(ordcomb))]
    print(chklist)
    print(min(chklist))
    tmp = chklist.index(min(chklist))
    print(tmp)

    res = ''
    for ordnum in ordcomblist[tmp]:
        res += chr(ordnum)

    return res

print(solution('hot'))