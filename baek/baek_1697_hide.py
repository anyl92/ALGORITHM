import sys
sys.stdin = open('1697.txt', 'r')


def bfs(n):
    global time

    q = [n+1, n-1, n*2]
    while q:
        for _ in range(len(q)):
            cur = q.pop(0)
            if cur > 100010 or cur <= 0:
                continue
            if cur == K:
                return time

            if not V[cur]:
                V[cur] = [cur + 1, cur - 1, cur * 2]
                q.extend(V[cur])

        time += 1


N, K = map(int, input().split())
V = [[] for _ in range(1000001)]
time = 1
if N == K:
    print(0)
elif N > K:
    print(N - K)
else:
    print(bfs(N))
