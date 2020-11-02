import sys
sys.stdin = open('5212.txt', 'r')

R, C = map(int, input().split())
L = [list(input()) for _ in range(R)]
delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]

state_list = []
for r in range(R):
    for c in range(C):
        if L[r][c] == 'X':
            cnt = 0
            if r == 0:
                cnt += 1
            if r == R - 1:
                cnt += 1
            if c == 0:
                cnt += 1
            if c == C - 1:
                cnt += 1

            if cnt >= 3:
                L[r][c] = 'O'
                continue

            for rr, cc in delta:
                rr += r
                cc += c

                if 0 <= rr < R and 0 <= cc < C:
                    if L[rr][cc] == '.':
                        cnt += 1
                        if cnt >= 3:
                            L[r][c] = 'O'
                            break
            else:
                state_list.append([r, c])

sort_list_r = sorted(state_list)
min_r = sort_list_r[0][0]
max_r = sort_list_r[-1][0]

sort_list_c = sorted(state_list, key=lambda x: x[1])
min_c = sort_list_c[0][1]
max_c = sort_list_c[-1][1]

res_list = []
for y in range(min_r, max_r+1):
    tmp_list = []
    for x in range(min_c, max_c+1):
        tmp_list.append(L[y][x])
    res_list.append(tmp_list)

for res in res_list:
    for r in res:
        if r == 'O':
            print('.', end='')
        else:
            print(r, end='')
    print()

'''
for문 돌면서 X일때 3면이 바다인지 확인하고 지운다.
그리고 그 배열에서 x, y값이 가장 먼저 나오는 곳을 찾아서(라인별로 쭉 찾음
x좌표에서는 y값, y좌표에서는 x값을 뽑아 배열의 시작점을 만듬

해당 좌표가 X면 3면을 조사하고 O으로 바꾼다 
바뀌지 않으면 리스트에 넣는다.
리스트에서 가장 작은 x, y, 가장 큰 x, y를 구하면?
'''
