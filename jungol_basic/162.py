import sys
sys.stdin = open('input.txt', 'r')

a = list(map(int, input().split()))
b = [0] * 10

b[0] = a[0]
b[1] = a[1]
for i in range(2, len(b)):
    tmp = b[i-2]+b[i-1]
    if tmp > 9:
        tmp %= 10
    b[i] = tmp
for i in b:
    print(i, end=' ')

#3 5 8 3 1 4 5 9 4 3