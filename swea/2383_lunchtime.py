import sys
sys.stdin = open('2383.txt', 'r')


def step_down(dist, step):
    # print('step', step)
    # print(dist)
    down = []
    cnt = dist[0]

    while dist:
        while dist and dist[0] == cnt and len(down) < 3:
            down.append(step + 1)
            dist.pop(0)

        for k in range(len(down)):
            down[k] -= 1

            if down[k] <= 0 and dist and dist[0] <= cnt:
                down[k] = step
                dist.pop(0)

        for i in down:
            if i <= 0:
                down.pop(down.index(i))

        cnt += 1
    if down:
        return cnt + max(down)
    else: return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 하상우좌
    res = 9999999999

    per, step = [], []
    for i in range(N):
        for j in range(N):
            if L[i][j] == 1:
                per += [[i, j]]
                continue
            if L[i][j]:
                step += [[i, j]]

    # 계단이 두개니까 한 계단에서 부분집합을 뺄거야
    pws = [[]]
    for e in per:
        pws += [x + [e] for x in pws]

    while pws:
        step1_dist = []
        step2_dist = []
        step1 = pws.pop(0)
        step2 = []
        for c in per:
            step2 += [c]

        for comb1 in step1:
            for comb2 in step2:
                if comb1 == comb2:
                    step2.pop(step2.index(comb2))
                    break

        # 거리 구함
        for s1 in step1:
            step1_dist += [abs(s1[0]-step[0][0]) + abs(s1[1]-step[0][1])]
        for s2 in step2:
            step2_dist += [abs(s2[0] - step[1][0]) + abs(s2[1] - step[1][1])]
        # print()
        # 계단 내려감
        step1_cnt, step2_cnt, step_cnt = 0, 0, 0
        if step1_dist:
            step1_cnt = step_down(sorted(step1_dist), L[step[0][0]][step[0][1]])
        if step2_dist:
            step2_cnt = step_down(sorted(step2_dist), L[step[1][0]][step[1][1]])

        step_cnt = max(step1_cnt, step2_cnt)
        # print(step_cnt)
        # if step1_cnt >= step2_cnt:
        #     step_cnt = step1_cnt
        # else:
        #     step_cnt = step2_cnt

        if res > step_cnt:
            res = step_cnt

    print("#%d %d" % (tc, res))