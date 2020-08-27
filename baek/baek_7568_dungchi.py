import sys
sys.stdin = open('dungchi_input.txt', 'r')

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
res = [0] * N

for i in range(len(L)):
    cnt = 1
    for j in range(len(L)):
        if i != j:
            if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
                cnt += 1
    res[i] = cnt

for i in res:
    print(i, end=' ')