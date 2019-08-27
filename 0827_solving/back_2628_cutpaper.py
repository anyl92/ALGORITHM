import sys
sys.stdin = open('input.txt', 'r')
garo, sero = map(int, input().split())
cut = int(input())
L = [list(map(int, input().split())) for _ in range(cut)]
print(garo, sero, cut, L)
y = []
x = []
comp = []
for k in range(cut):
    if L[k][0] == 1: # sero
        y.append(L[k][1])
    elif L[k][0] == 0: # garo
        x.append(L[k][1])
print(x, y)
arr_count = garo * sero

tmp = (min(x)+1) * (min(y)+1)
comp.append(tmp)
tmp = (min(x)+1) * min(y)+1 - tmp
comp.append((tmp))