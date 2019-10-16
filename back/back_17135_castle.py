import sys
sys.stdin = open('17135.txt', 'r')


def attack(T):
    dir = [(0, -1), (-1, 0), (0, 1)]
    attack_list = []
    cnt = 0

    for r in range(N - 1, -1, -1):
        for c in T:
            if L[r][c]:
                attack_list += [(r, c)]
            else:
                dcnt = 1
                q = [[r, c]]
                flag = True

                while q and flag:
                    if dcnt == AD:
                        break

                    for _ in range(len(q)):
                        cur = q.pop(0)

                        for d in dir:
                            rr = cur[0] + d[0]
                            cc = cur[1] + d[1]
                            if 0 <= rr < N and 0 <= cc < M:
                                if L[rr][cc]:
                                    attack_list += [(rr, cc)]
                                    flag = False
                                    break
                                else:
                                    q.append([rr, cc])
                        if not flag:
                            break
                    dcnt += 1

        for x, y in set(attack_list):
            if L[x][y]:
                cnt += 1
                L[x][y] = 0
    return cnt


def located(k, s):
    global res
    if k == 3:
        cnt = attack(T)

        if res < cnt:
            res = cnt

        for i in range(N):
            for j in range(M):
                L[i][j] = CL[i][j]
        return

    for i in range(s, M+(k-3)+1):
        T[k] = P[i]
        located(k+1, i+1)


N, M, AD = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
CL = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        CL[i][j] = L[i][j]

res = 0

T = [0, 0, 0]
P = [i for i in range(M)]
located(0, 0)
print(res)