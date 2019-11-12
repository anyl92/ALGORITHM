import sys
sys.stdin = open('2383.txt', 'r')


def step_down(dist, step):
    cnt = dist[0]
    full = []

    if len(full) < 2:
        forcnt = 1
        for d in range(len(dist)-1):
            if dist[d] != dist[d+1]:
                break
            else:
                forcnt += 1

    if len(full) < 3 and cnt == dist[0]:
        for _ in range(forcnt):
            full.append(step)
            dist.pop(0)

    elif len(full) < 3 and cnt != dist[0]:
        for _ in range(forcnt):
            full.append(step-1)
            dist.pop(0)

    cnt += 1
    for f in range(len(full)):
        full[f] -= 1




    # cnt = 0
    # full = []
    # fullmax = []
    # mindist = dist[0]
    # stepval = L[step[0]][step[1]]
    #
    # for k in range(len(dist)-1):
    #     comp = dist[k + 1] - dist[k]
    #     if comp == 0 or comp == 1:
    #         continue
    #     else:
    #         cnt += comp
    #
    # while True:
    #     if len(full) < 3 and dist:
    #         popval = dist.pop(0)
    #         full.append(popval)
    #         fullmax.append(popval + stepval + 1)
    #
    #     while len(full) < 3 and dist and popval == dist[0]:
    #         dist.pop(0)
    #         full.append(popval)
    #         fullmax.append(popval + stepval + 1)
    #
    #     for f in range(len(full)):
    #         full[f] += 1
    #
    #     while full and fullmax[0] == full[0]:
    #         full.pop(0)
    #         fullmax.pop(0)
    #         if not full and not dist:
    #             return mindist + cnt + 1
    #     cnt += 1


def step_find(q, step):
    vst = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 1
    while q:
        for _ in range(len(q)):
            r, c = q.pop(0)
            for d in dir:
                rr = r + d[0]
                cc = c + d[1]
                if 0 <= rr < N and 0 <= cc < N and not vst[rr][cc]:
                    if rr == step[0] and cc == step[1]:
                        return cnt
                    vst[rr][cc] = 1
                    q.append([rr, cc])
        cnt += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 하상우좌
    res = 9999

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

        print(step1, step2)

        # 구한 step1과 step2에서 bfs 동작 - 거리 계산
        for s1 in step1:
            step1_dist += [step_find([s1], step[0])]
        for s2 in step2:
            step2_dist += [step_find([s2], step[1])]

        # 계단 내려감
        step1_cnt, step2_cnt, step_cnt = 0, 0, 0
        if step1_dist:
            step1_cnt = step_down(sorted(step1_dist), step[0])
        if step2_dist:
            step2_cnt = step_down(sorted(step2_dist), step[1])
        if step1_cnt >= step2_cnt:
            step_cnt = step1_cnt
        else:
            step_cnt = step2_cnt
        print(step1_cnt, step2_cnt)
        if res > step_cnt:
            res = step_cnt

        # 초기화
        step2 = []
        for c in per:
            step2 += [c]
    print(res, 'res')