import sys
sys.stdin = open('15686.txt', 'r')

import itertools

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

chickenhouse, home = [], []
for c in range(N):
    for r in range(N):
        if L[c][r] == 2:
            chickenhouse += [(r, c)]
        if L[c][r] == 1:
            home += [(r, c)]

comb = list(itertools.combinations(chickenhouse, M))

cd_sum = 99999
for ckh in comb:  # 치킨집 총 조합
    cd_list = []
    for h in home:  # 각 홈에서 치킨집을 찾음
        cd = 99999
        for c in ckh:  # 치킨집 하나씩
            tmp = abs((h[0]+1)-(c[0]+1)) + abs((h[1]+1)-(c[1]+1))  # 치킨거리
            if tmp < cd:
                cd = tmp  # 치킨거리 min찾음
        cd_list += [cd]  # min치킨거리 배열에추가 6집에서 각각 치킨집 거리
    if sum(cd_list) < cd_sum:
        cd_sum = sum(cd_list)
print(cd_sum)