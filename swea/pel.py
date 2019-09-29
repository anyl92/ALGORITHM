#4861
import sys
sys.stdin = open('pel_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(input()) for _ in range(N)]

    def find_pel(N, i):
        res = [0] * M
        x = 0
        y = 0
        while x < N or y < N:
            j = M-i-1
            if L[x][i] == L[x][j]:
                res[i] = L[x][i]
                res[j] = L[x][j]
            elif L[i][y] == L[j][y]:
                res[i] = L[i][y]
                res[j] = L[j][y]
            x += 1
            y += 1
            else:
                break
        return res

    for _ in range(N-M+1):
        if M % 2:  # 홀수
            for i in range(N//2 +1):
                print(find_pel(N,i))
        if M % 2 == 0:  # 짝수
            for i in range(N//2):
                print(find_pel(N,i))
                
"""
while res != 글자수 될때까지
1. 글자수 N-M+1
2. x, y 값
3. 짝, 홀
졸려
"""