import sys
sys.stdin = open('14890.txt', 'r')

N, L = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
waylist = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        waylist[i][j] = map[i][j]

for j in range(N):
    tmp = []
    for i in range(N):
        tmp.append(map[i][j])
    waylist.append(tmp)


def firstchk(way):
    for w in range(N-1):
        if abs(way[w] - way[w + 1]) >= 2:
            return 1
    for w in way:
        if way[0] != w:
            return -1  # 돌아라
    return 0


def const_right_up(way, w):
    for l in range(1, L+1):  # 왼쪽을 이만큼 볼거고
        if way[w] != way[w - l]:  # 걔들이 나랑 다르면 나가
            return 1
    return 0


def const_right_down(way, w, chk):
    for l in range(2, L + 2):
        if chk != way[w + l]:  # 오른쪽을 볼거 다르면 나가
            return 1
    return 0


def const_left_up(way, w):
    for l in range(1, L+1):  # 나부터 볼거니까
        if way[w] != way[w - l]:
            return 1
    return 0


def const_left_down(way, w, chk):
    for l in range(2, L + 2):
        if chk != way[w + l]:
            return 1
    return 0


def lastchk(way):
    if (L*2) + 2 <= N:
        for w in range(N - (L*2)):
            if way[w + (L * 2)] == way[w]:
                chk = way[w + 1]
                if chk == way[w] - 1:  # 다음애가 1작으면
                    for l in range(L*2):
                        if chk != way[w + l]:  # 모두 같지 않으면 나가
                            return 1
    return 0


poplist = []
for way in waylist:
    chknum = firstchk(way)
    if chknum == 0:
        continue
    elif chknum == 1:
        poplist.append(way)
    elif chknum == -1:
        chklist = [0, 0, 0, 0]
        for w in range(L, N-1):
            chk = way[w + 1]  # 다음 애를 볼거임
            if way[w]+1 == chk:  # 나보다 크면
                chklist[0] = const_right_up(way, w)

            chk = way[w - 1]  # 이전 애를 볼거임
            if way[w]-1 == chk:  # 나보다 작으면
                chklist[1] = const_left_down(way, w, chk)

        for w in range(N - L):
            chk = way[w + 1]  # 다음 애를 볼거임
            if way[w]-1 == chk:  # 나보다 작으면
                chklist[2] = const_right_down(way, w, chk)

            chk = way[w - 1]  # 이전 애를 볼거임
            if way[w]+1 == chk:  # 나보다 크면
                chklist[3] = const_left_up(way, w)

        if sum(chklist) != 0:
            chknum = lastchk(way)
            if chknum:
                poplist.append(way)

for p in poplist:
    waylist.remove(p)
print(len(waylist), waylist)




# def const(way):
#     for x in way[:K]:
#         if x != way[0]:
#             return 1
#     for x in way[N-K:]:
#         if x != way[-1]:
#             return 1
#
#
# def const1(way):
#     for w in range(N - K):
#         chknum = way[w + 1]  # 내 다음애
#         if abs(chknum - way[w]) >= 2:
#             return 1
#         if chknum - way[w] == 1:  # 다음애가 1큼
#             for k in range(K):
#
#                 if chknum != way[w - k]:
#                     return 1
#         if way[w] - chknum == 1:  # 다음애가 1작음
#             for k in range(2, K + 1):
#                 if chknum != way[w + k]:
#                     return 1
#     return 0
#
#
# def const2(way):
#     for w in range(K, N):
#         chknum = way[w - 1]  # 내 이전애
#         if abs(chknum - way[w]) >= 2:
#             return 1
#         if chknum - way[w] == 1:  # 이전애가 1큼
#             for k in range(2, K+1):
#                 if chknum != way[w - k]:
#                     return 1
#         if way[w] - chknum == 1:  # 이전애가 1작음
#             for k in range(2, K+1):
#                 if chknum != way[w - k]:
#                     return 1
#     return 0
#
#
# def const3(way):
#     if (K*2) + 2 <= N:
#         for w in range(N - (K*2)):
#             chknum = way[w + 1]
#             if chknum == way[w] - 1:
#                 for k in range(K*2):
#                     if chknum != way[w+k]:
#                         return 1
#     return 0
