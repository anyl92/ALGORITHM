import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    # L = [input().split() for _ in range(N)]
    D = {}
    for _ in range(N):
        value, key = input().split()
        if D.get(key):
            D[key].append(value)
        else:
            D[key] = [value]

    for i in range(len(D)):
        for j in range(len(D[i])):
            D[i][j]
    print(N, D)

