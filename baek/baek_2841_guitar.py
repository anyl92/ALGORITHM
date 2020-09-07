import sys
sys.stdin = open('2841.txt', 'r')

N, P = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

guitar = [[] for _ in range(6)]
res = 0

for melody in L:
    cur = melody[0] - 1
    fret = melody[1]
    while guitar[cur] and max(guitar[cur]) > fret:
        guitar[cur].pop()
        res += 1
    if guitar[cur] and max(guitar[cur]) == fret:
        continue
    else:
        guitar[cur].append(melody[1])
        res += 1

print(res)
