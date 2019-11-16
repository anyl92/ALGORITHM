import sys
sys.stdin = open('14501.txt', 'r')
#
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ti = [0]*N
    Pi = [0]*N
    Si = [0]*N
    for i in range(N):
        Ti[i], Pi[i] = map(int, input().split())
    maxi = 0


    def solve(k):
        global maxi
        if k == N:
            for i in range(N):
                if Si[i]:
                    for j in range(i+1, i+Ti[i]):
                        if j >= N or Si[j]:
                            return
            tsum = 0
            for i in range(N):
                if Si[i]:
                    tsum += Pi[i]
            if tsum > maxi:
                maxi = tsum

        else:
            Si[k] = 1
            solve(k+1)
            Si[k] = 0
            solve(k+1)


    solve(0)
    print(maxi)