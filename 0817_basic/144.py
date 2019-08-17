import sys
sys.stdin = open('input.txt', 'r')

a = int(input())
n = 1 + (2 * (a-1))
for j in range(1, n+1, 2):
    print(' '*(n-j) + '*'*j)


# n = int(input())
# for i in range(n):
#     for j in range(n * 2 - i * 2 - 2):
#         print(' ', end='')
#     for j in range(i * 2 + 1):
#         print('*', end='')
#     print()