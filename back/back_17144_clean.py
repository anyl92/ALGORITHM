import sys
sys.stdin = open('17144.txt', 'r')

import collections

R, C, T = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(R)]

CL = [[0]*C for _ in range(R)]
for y in range(R):
    for x in range(C):
        CL[y][x] = L[y][x]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

def diffusion(r, c):
    tmp = L[r][c]  # 현재좌표 미세먼지값
    dif_dq = collections.deque([])  # 확산좌표 저장
    cnt = 0  # 계산식 구하기 위해

    for d in dir:  # 방향
        rr, cc = r + d[0], c + d[1]  # 다음 좌표
        if 0 <= rr < R and 0 <= cc < C and L[rr][cc] != -1:  # 범위 내에 -1이 아니면
            dif_dq.append((rr, cc))  # 뿌릴 배열에 저장
            cnt += 1  # len() 대신 써봄

    calc = tmp - ((tmp//5)*(cnt))
    if CL[r][c] > L[r][c]:  # 카피값에 추가된 미세먼지가 있으면
        CL[r][c] = CL[r][c]-L[r][c] + calc
    else:
        CL[r][c] = calc  # 없으면 걍 바꿈

    for rr, cc in dif_dq:  # 뿌릴 배열길이만큼
        CL[rr][cc] += tmp//5  # 계산해서 뿌림


def clean(loca):
    for k in [[3, 0, 2, 1], [3, 1, 2, 0]]:  # 방향 for
        r, c = loca.pop(0)  # 첫번째부터 팝해서 r, c 좌표 줌
        y, x = r, c  # 복사
        pre = 0
        for d in k:  # 방향을 d로 받음
            while (y + dir[d][0], x + dir[d][1]) != (r, c):  # 다음 좌표가 처음 좌표랑 같으면 끝내게
                yy, xx = y + dir[d][0], x + dir[d][1]
                if -1 <= yy <= R and -1 <= xx <= C:
                    # 벽에 부딪히면 나가서 다음 방향
                    if d == 3 and xx == C:
                        break
                    if d == 2 and xx == -1:
                        break
                    if d == 1 and yy == R:
                        break
                    if d == 0 and yy == -1:
                        break

                    tmp = CL[yy][xx]
                    CL[yy][xx] = pre
                    pre = tmp  # 공기 순환

                    y, x = yy, xx  # 다음 값
    return


clean_location = []  # 청정기
for _ in range(T):  # 반복 시간
    for i in range(R):  # 행
        for j in range(C):  # 열
            if L[i][j] != -1 and L[i][j]:  # -1이 아니고 값이 있다면
                diffusion(i, j)  # 뿌리러 간다
            elif L[i][j] == -1 and len(clean_location) != 2:  # 값이 -1이고 청정장소가 2개가 아니면
                clean_location += [(i, j)]

    clean(clean_location)  # 행렬 한바퀴 다 돌고 청정기 돌리러

    for y in range(R):
        for x in range(C):
            L[y][x] = CL[y][x]  # 초기화

res = 0
for i in range(R):
    for j in range(C):
        if CL[i][j]:
            res += CL[i][j]
print(res + 2)  # -1이 두개 있어서