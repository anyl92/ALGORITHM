import sys
sys.stdin = open('input.txt', 'r')

#a = list(map(int, input().split()))
a = int(input())
i = j = 1
while j % 10 != 0:
    j = a * i
    if j > 99:
        break
    print(j, end=' ')
    i += 1
