import sys
sys.stdin = open('input.txt', 'r')

N, S = map(int,input().split())
L = list(map(int, input().split()))

r = [[]]
for e in L:
    r += [x+[e] for x in r]
r.pop(0)

cnt = 0
for i in r:
    summ = 0
    for j in i:
        summ += j
    if summ == S:
        cnt += 1
print(cnt)