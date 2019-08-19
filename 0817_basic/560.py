import sys
sys.stdin = open('input.txt', 'r')

a = list(map(int,input().split()))
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a[0])
