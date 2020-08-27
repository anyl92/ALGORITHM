import sys
sys.stdin = open('input.txt', 'r')

N, M = list(map(int, input().split()))
perm_list = sorted(list(map(int, input().split())))

def perm(k):
    flag = 0
    if k == M:
        for i in range(M):
            print(T[i], end=' ')
        print()
        return
    
    for i in range(N):
        T[k] = perm_list[i]
        perm(k+1)
        
T = [0] * M
perm(0)


'''
N, M = map(int, input().split())
data = sorted(list(map(int, input().split())))

def perm(arr, r):
  global N, M
  if r == M:
    print(*arr, sep=" ")
    return
  for i in range(N):
    arr[r] = data[i]
    perm(arr, r+1)

array = [0] * M
perm(array, 0)
'''