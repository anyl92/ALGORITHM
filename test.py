import sys
sys.stdin = open('input.txt', 'r')

N, M = list(map(int, input().split()))

import math
C = math.factorial(N) // math.factorial(N-M) * math.factorial(M)

perm_list = sorted(list(map(int, input().split())))
pre_list = []

def perm(k):
    global pre_list
    if k == M:
        if pre_list != T:
            for i in range(M):
                print(T[i], end=' ')
            print()
            pre_list = []
        else:
            return
        
        for i in range(len(T)):
            pre_list.append(T[i])
        return
    
    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        T[k] = perm_list[i]
        perm(k+1)
        visited[i] = 0

visited = [0] * N
T = [0] * M
perm(0)