import sys
sys.stdin = open('11286.txt', 'r')

N = int(input())
L = [int(input()) for _ in range(N)]


res = []
for x in L:
    if x != 0:
        res.append([x, abs(x)])
    else:
        if res:
            if len(res) > 1:
                res.sort(key=lambda y: (y[1], y[0]))
            tmp, _ = res.pop(0)
            print(tmp)
        else:
            print(0)
