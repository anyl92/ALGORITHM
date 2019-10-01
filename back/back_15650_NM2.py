import sys
sys.stdin = open('input.txt', 'r')

def perm(k):
    if k == M:
        if sorted(T) == T:
            for i in range(M):
                print(T[i], end=' ')
            print()
        return

    for i in range(1, N+1):  # 순열 찾을 범위
        if V[i]: continue
        V[i] = 1
        T[k] = i
        perm(k+1)
        V[i] = 0

N, M = map(int, input().split())  # N까지의 자연수 중 M개
V = [0] * (N+1)  # 순열을 찾을 수의 범위
T = [0] * (M)  # 내가 필요한 조건 수의 범위
perm(0)
