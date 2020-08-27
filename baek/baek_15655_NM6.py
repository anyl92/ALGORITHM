import sys
sys.stdin = open('input.txt', 'r')

N, M = list(map(int, input().split()))
perm_list = sorted(list(map(int, input().split())))

def perm(k):
    flag = 0
    if k == M:
        for i in range(M-1):
            if T[i] >= T[i+1]:
                break
        else:
            flag = 1

        if flag:
            for i in range(M):
                print(T[i], end=' ')
            print()
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