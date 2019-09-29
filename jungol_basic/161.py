import sys
sys.stdin = open('input.txt', 'r')

a = list(map(int, input().split()))
count = [0] * 11
for i in a:
    j = 10
    while True:
        if not i:
            break
        if i // 10 == j:
            count[j] += 1
            break
        j -= 1

for j in range(10, -1, -1):
    if count[j]:
        print('%d : %d' % ((j-1+1)*10, count[j]), 'person')