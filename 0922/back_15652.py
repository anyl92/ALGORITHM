import sys
sys.stdin = open('input.txt', 'r')

def perm(k):
    if k == M:
        if sorted(T) == T:
            for i in range(M):
                print(T[i], end=' ')
            print()
        return

    for i in range(1, N+1):
        T[k] = i
        perm(k+1)

N, M = map(int, input().split())
T = [0] * (M)
perm(0)