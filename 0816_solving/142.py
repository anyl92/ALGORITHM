import sys
sys.stdin = open('input.txt', 'r')

a = int(input())
i = 1
while True:
    print('*'*i)
    i += 1
    if i == a:
        while i != 0:
            print('*'*i)
            i -= 1
        break

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end='')
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         print("*", end = '')
#     print()
