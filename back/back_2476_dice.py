import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

maxx = 0
for i in range(len(L)):
    if len(set(L[i])) == 1:
        tmp = L[i][0] * 1000 + 10000
        if maxx < tmp:
            price = tmp
            maxx = tmp
    elif len(set(L[i])) == 2:
        for j in range(3):
            for k in range(j+1, 3):
                if L[i][j] == L[i][k]:
                    tmp = L[i][j] * 100 + 1000
                    if maxx < tmp:
                        price = tmp
                        maxx = tmp
    else:
        tmp = max(L[i]) * 100
        if maxx < tmp:
            price = tmp
            maxx = tmp
print(price)