import sys
sys.stdin = open('2816.txt', 'r')

N = int(input())
L = [input() for _ in range(N)]
res = []


def kbs():
    cur = 0
    next_channel = ''

    while L[0] != 'KBS1':
        if cur + 1 < N:
            next_channel = L[cur + 1]

        if cur == 0 and next_channel == 'KBS1':
            L[cur], L[cur + 1] = L[cur + 1], L[cur]
            cur += 1
            res.append('3')
        elif L[cur] == 'KBS1':
            L[cur], L[cur - 1] = L[cur - 1], L[cur]
            cur -= 1
            res.append('4')
        else:
            cur += 1
            res.append('1')

    while L[1] != 'KBS2':
        if cur + 1 < N:
            next_channel = L[cur + 1]

        if cur == 0:
            cur += 1
            res.append('1')
        elif cur == 1 and next_channel == 'KBS2':
            L[cur], L[cur + 1] = L[cur + 1], L[cur]
            cur += 1
            res.append('3')
        elif L[cur] == 'KBS2':
            L[cur], L[cur - 1] = L[cur - 1], L[cur]
            cur -= 1
            res.append('4')
        else:
            cur += 1
            res.append('1')


kbs()
for r in res:
    print(r, end='')
