import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
L = list(map(int, input().split()))

i = 0
while i < len(L):
    if M < L[i]:
        i += 1
        continue
    else:
        L.pop(i)
        M += 1
        i = 0

print(M)

