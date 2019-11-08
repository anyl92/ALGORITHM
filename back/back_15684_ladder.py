import sys
sys.stdin = open('15684.txt', 'r')

import itertools, collections
W, M, H = map(int, input().split())
L = [[0 for _ in range(W)] for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    L[a-1][b-1] += 2
    L[a-1][b] += 3
# for l in L:
#     print(l)


def check():  # r, c
    for c in range(W):
        cc = c  # c copy
        r = 0
        while cc < W and r < H:
            while r + 1 < H and not L[r][cc]:
                r += 1
            if L[r][cc] == 2:
                if L[r][cc+1] == 3:
                    r += 1
                    cc += 1
                    continue
            if L[r][cc] == 3:
                if L[r][cc-1] == 2:
                    r += 1
                    cc += -1
                    continue
            r += 1
        if c != cc:
            return False
    return True


def construction(comb):
    cnt = 0
    for c in comb:
        w, h = c[0], c[1]
        if L[h][w]:
            break
        else:
            L[h][w] = 2
            L[h][w + 1] = 3
            cnt += 1
    else:
        if check():
            return len(comb)

    for c in comb[:cnt]:
        w, h = c[0], c[1]
        L[h][w] = 0
        L[h][w + 1] = 0


def make_ladder():
    ladder_list = []
    for h in range(H):
        for w in range(W-1):
            if not L[h][w]:
                if not L[h][w+1]:
                    ladder_list += [(w, h)]

    for k in range(1, 4):
        ladder_comb = collections.deque(itertools.combinations(ladder_list, k))
        while ladder_comb:
            tmp = construction(ladder_comb.popleft())  # 조합 한 쌍씩
            if tmp:
                return tmp
    return -1


def main():
    if check():
        return print(0)
    return print(make_ladder())


main()
# 271664	1836