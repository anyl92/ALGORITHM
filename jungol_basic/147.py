import sys
sys.stdin = open('input.txt', 'r')

a = int(input())
l = 0
for i in range(a):
    for j in range(i):
        print(' ', end=' ')
    for k in range(a-i):
        print(l+1, end=' ')
        l += 1
    print()


# n = int(input())
# snum = 1
# for i in range(n):
#     for j in range(i):
#         print(' ', end = ' ')
#     for j in range(n - i):
#         print(snum, end = ' ')
#         snum += 1
#     print()
