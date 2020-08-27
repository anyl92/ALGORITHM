import sys
sys.stdin = open('17822.txt', 'r')

N, M, T = map(int, input().split())
numlist = [list(map(int, input().split())) for _ in range(N)]
ctrlist = [list(map(int, input().split())) for _ in range(T)]

for curl in ctrlist:
    memory = []
    dir = curl[1]
    for _ in range(curl[2]):
        for repeat in range(1, len(numlist)+1):
            if repeat % curl[0] == 0:
                if dir == 0:  # 시계
                    tmp = numlist[repeat-1].pop()
                    numlist[repeat-1].insert(0, tmp)
                else:  # 반시계
                    tmp = numlist[repeat-1].pop(0)
                    numlist[repeat-1].append(tmp)
    print(numlist)
    removelist = []
    for i in range(N-1):
        for j in range(M):
            if numlist[i][j] and numlist[i][j] == numlist[i+1][j]:
                removelist += [(i, j)]
                removelist += [(i+1, j)]
    for i in range(N):
        for j in range(M-1):
            if numlist[i][j] and numlist[i][j] == numlist[i][j+1]:
                removelist += [(i, j)]
                removelist += [(i, j+1)]
            if numlist[i][0] and numlist[i][0] == numlist[i][-1]:
                removelist += [(i, 0)]
                removelist += [(i, M-1)]
    print(removelist)
    if removelist:
        for k in set(removelist):
            numlist[k[0]][k[1]] = 0
        print(numlist)
    else:
        calclist = sum(numlist, [])
        res, cnt = 0, 0
        for calc in calclist:
            if calc:
                res += calc
                cnt += 1
        if cnt:
            res /= cnt
        print(res)
        for num in numlist:
            for n in range(M):
                if num[n] and num[n] < res:
                    num[n] += 1
                elif num[n] and num[n] > res:
                    num[n] -= 1
        print(numlist)
    print()
print(sum(sum(numlist, [])))