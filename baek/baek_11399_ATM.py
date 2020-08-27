import sys
sys.stdin = open('ATM_input.txt', 'r')

N = int(input())
L = list(map(int, input().split()))
L.sort()

res, total = 0, 0
for i in L:
    res += i
    total += res
print(total)