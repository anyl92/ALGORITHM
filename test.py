import sys
sys.stdin = open('input.txt', 'r')

N, M = list(map(int, input().split()))

import math
C = math.factorial(N) // math.factorial(N-M) * math.factorial(M)

perm_list = sorted(list(map(int, input().split())))
new_perm_list = []
for i in set(perm_list):
    new_perm_list.append(i)

def perm(k):
    if k == M:
        for i in range(M):
            print(T[i], end=' ')
        print()
        return
    
    for i in range(len(new_perm_list)):
        if visited[i] == 1:
            continue
        visited[i] = 1
        T[k] = new_perm_list[i]
        perm(k+1)
        visited[i] = 0

visited = [0] * N
T = [0] * M
perm(0)