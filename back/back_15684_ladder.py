import sys
sys.stdin = open('15684.txt', 'r')

import itertools, collections
W, M, H = map(int, input().split())
L = [[0 for _ in range(W)] for _ in range(H)]

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

    for k in range(1, len(ladder_list)+1):
        ladder_comb = collections.deque(itertools.combinations(ladder_list, k))
        print(ladder_comb)

        comb = ladder_comb.popleft()  # 조합 한 쌍



check()
# ok되면 리턴/끝
make_ladder()
# end