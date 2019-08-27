import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
arr = [[0 for _ in range(100)] for _ in range(100)]

for k in range(len(L)):
    for i in range(L[k][1], L[k][1]+10):
        for j in range(L[k][0], L[k][0]+10):
            arr[i][j] = 1
count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            count += 1
print(count)