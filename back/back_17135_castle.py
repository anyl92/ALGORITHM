import sys
sys.stdin = open('17135.txt', 'r')


def attack(r, T):  # 4, 0
    global cnt
    dir = [(0, -1), (-1, 0), (0, 1)]  # 좌 상 우
    attack_list = []

    for c in T:  # 궁수의 개수(3) 만큼 반복
        dcnt = 0
        q = []
        flag = True
        if L[r][c]:
            attack_list += [(r, c)]  # 현재위치에 적이 있으면 어택 배열에 추가
        else:
            q += [[r, c]]  # 현재위치 에서 q
            while flag:
                cur = q.pop()  # q를 꺼내서 좌표 지정
                r = cur[0]
                c = cur[1]
                for d in dir:  # 다음 방향들(3)을 탐색
                    if dcnt == AD-1:
                        flag = False
                        break
                    rr = r + d[0]
                    cc = c + d[1]
                    if 0 <= rr < N and 0 <= cc < M and L[rr][cc]:
                        attack_list += [(rr, cc)]
                        flag = False
                        break
                    elif 0 <= rr < N and 0 <= cc < M and L[rr][cc]==0:
                        q.append([rr, cc])  # q에 추가하여 다음 턴에 돈다
                dcnt += 1  # bfs 한 번 돌 때 마다 카운트

    for attack in attack_list:  # 한 번 턴에 죽일수 있는 적 리스트를 0으로 만들어서
        L[attack[0]][attack[1]] = 0  # 다음 턴에 안 보게 만들어준다

    return attack_list


def located(k, s):
    global res
    total_attack_list = []
    if k == 3:
        cnt = 0

        for turn in range(N-1, -1, -1):
            total_attack_list += attack(turn, T)
            cnt = len(set(total_attack_list))

        if res < cnt:
            res = cnt

        for i in total_attack_list:
            L[i[0]][i[1]] = 1

        return res

    for i in range(s, M+(k-3)+1):
        T[k] = P[i]
        located(k+1, i+1)


N, M, AD = map(int, input().split())  # 행, 열, 공격 거리
L = [list(map(int, input().split())) for _ in range(N)]
CL = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        CL[i][j] = L[i][j]

res = 0

T = [0, 0, 0]  # 조합이 저장될 배열
P = [i for i in range(M)]  # 조합을 구할 수를 구한 배열 (0, 1, 2, 3, 4)

located(0, 0)
print(res)