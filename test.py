def step_down(dist):
    step = 7

    cnt = dist[0]
    full = []

    while dist:
        if len(full) < 2:
            forcnt = 1
            for d in range(len(dist) - 1):
                if dist[d] != dist[d + 1]:
                    break
                else:
                    forcnt += 1

        if len(full) < 3 and cnt == dist[0]:
            for _ in range(forcnt):
                full.append(step)
                dist.pop(0)

        elif len(full) < 3 and cnt != dist[0]:
            for _ in range(forcnt):
                full.append(step - 1)
                dist.pop(0)

        cnt += 1
        for f in range(len(full)):
            full[f] -= 1

dist = [3, 6, 7, 8]
step_down(dist)