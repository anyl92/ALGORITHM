import sys
sys.stdin = open('input.txt', 'r')

a = int(input())
n = a+a-2
for i in range(1, a+1):
    print(' '*n, end='')
    n-=2
    for j in range(0, i):
        print(j+1, end=' ')
    print()


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(' ', end=' ')
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()
