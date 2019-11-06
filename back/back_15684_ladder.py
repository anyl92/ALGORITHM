import sys
sys.stdin = open('15684.txt', 'r')

import itertools

W, M, H = map(int, input().split())
print(W, M, H)

L = [[0 for _ in range(W)] for _ in range(H)]
print(L)

for _ in range(M):
    a, b = map(int, input().split())
    L[a-1][b-1] += 2
    L[a-1][b] += 3
for l in L:
    print(l)


def check():
    return


def make_ladder():
    ladder_list = []
    for h in range(H):
        for w in range(W-1):
            if not L[h][w]:
                if not L[h][w+1]:
                    ladder_list += [(w, h)]
    print(ladder_list)

    for ladder in ladder_list:
        L[ladder[1]][ladder[0]] = 2
        L[ladder[1]][ladder[0] + 1] = 3
        check()
        L[ladder[1]][ladder[0]] = 0
        L[ladder[1]][ladder[0] + 1] = 0


    return ladder_list


def comb(ladder):
    for k in range(2, len(ladder)+1):
        ladder_comb = list(itertools.combinations(ladder, k))
        # print(ladder_comb)



check()
# ok되면 리턴/끝
ladder = make_ladder()
check()
# ok되면 리턴/끝
comb(ladder)
check()
# end