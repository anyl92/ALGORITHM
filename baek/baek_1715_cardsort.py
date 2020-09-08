import sys
sys.stdin = open('1715.txt', 'r')

N = int(input())
L = sorted([int(input()) for _ in range(N)])

for x in range(N-1):
    L[x+1] = L[x] + L[x+1]
print(sum(L)-L[0])