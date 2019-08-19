import sys
sys.stdin = open('input.txt', 'r')

n = 14 #int(input())
N = n + n-1
k = n-2
l = 3
for i in range(N):
    print(' '*i + '*'*N)
    N -= 2
    if N < 0:
        break
for j in range(n-1):
    print(' '*(k) + '*'*l)
    k -= 1
    l += 2

# n = int(input())
# for i in range(n):
#     for j in range(i):
#         print(' ', end='')
#     for j in range(n * 2 - 1 - i * 2):
#         print('*', end='')
#     print()
# for i in range(1, n):
#     for j in range(n - i - 1):
#         print(' ', end='')
#     for j in range(i * 2 + 1):
#         print('*', end='')
#     print()
