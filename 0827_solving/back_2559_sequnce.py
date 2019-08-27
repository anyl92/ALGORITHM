import sys
sys.stdin = open('input.txt', 'r')
N, K = map(int, input().split())
L = list(map(int, input().split()))
ans = 0
for i in range(K):
    ans += L[i]
sum = ans
for i in range(1, N-K+1):
    sum -= L[i-1]
    sum += L[i+K-1]
    if sum > ans:
        ans = sum
print(ans)