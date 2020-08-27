import sys
sys.stdin = open('14501.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    maxi = 0


    def recul(k, v):  # 날짜, 비용
        global maxi

        if k == N:
            if v > maxi:
                maxi = v
            return

        if k + L[k][0] <= N:
            recul(k+L[k][0], v+L[k][1])
            recul(k + 1, v)
        else:
            recul(k+1, v)


    recul(0, 0)
    print(maxi)