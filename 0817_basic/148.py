import sys
sys.stdin = open('input.txt', 'r')

a = int(input())
for i in range(1, a):
    for _ in range(i):
        print('#', end=' ')
    print()
for j in range(a):
    print(' ' * (j * 2), end='')
    for _ in range(a):
        print('#', end=' ')
    a-=1
    print()


# n = int(input())
# for i in range(1, n):
#     for j in range(i):
#         print('#', end =' ')
#     print()
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(' ', end = ' ')
#     for j in range(i):
#         print('#', end =' ')
#     print()
