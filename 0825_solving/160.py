import sys
sys.stdin = open('input.txt', 'r')

a = list(map(int, input().split()))
b = [0]*6
for i in a:
    b[i-1] += 1
for i in range(1,len(b)+1):
    print('%d : %d' % (i, b[i-1]))