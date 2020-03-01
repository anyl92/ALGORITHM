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
    for w in range(N - 1):  # 2이상 차이나는지 체크
        if abs(way[w] - way[w + 1]) >= 2:
            return 1
    for w in way:  # 다 같은지 체크
        if way[0] != w:
            return -1  # 돌아라
    return 0


def const_up(way, w):
    global idxlist
    tmp = [w]
    for l in range(1, L):  # 나부터 볼거니까
        if w+l < N:
            tmp.append(w + l)
            if way[w] != way[w + l]:
                return 1
        else:
            return 1
    idxlist.extend(tmp)
    return 0


def const_down(way, w, chk):
    if w - 1 in idxlist:
        return 1
    for l in range(2, L+1):
        if w - l in idxlist:
            return 1
        if w - l >= 0:
            if chk != way[w - l]:
                return 1
        else:
            return 1
    return 0


chksum = 0
poplist = []
for way in waylist:
    idxlist = []
    chknum = firstchk(way)
    if chknum == 0:
        continue
    elif chknum == 1:
        poplist.append(way)
    elif chknum == -1:
        chksum = 0
        for w in range(1, N):
            pre = way[w - 1]
            if way[w] + 1 == pre:  # 이전애가 크면
                if const_up(way, w):
                    chksum += 1
                    break
            if way[w] - 1 == pre:  # 이전애가 작으면
                if const_down(way, w, pre):
                    chksum += 1
                    break
    if chksum != 0:
        poplist.append(way)

for p in poplist:
    if p not in waylist:
        continue
    waylist.remove(p)
print(len(waylist))