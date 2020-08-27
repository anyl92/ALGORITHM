import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

cnt, res = 0, 0
for i in range(len(coin)-1, -1, -1):
    if coin[i] > K:
        continue
    elif coin[i] == K:
        break
    else:
        while K >= res+coin[i]:
            res += coin[i]
            cnt += 1
print(cnt)