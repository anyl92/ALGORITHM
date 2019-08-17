import sys
sys.stdin = open('input.txt', 'r')

a = int(input())
ascii = 65
n = a
j = 0
while n > 0:
    for _ in range(n):
        print(chr(ascii), end=' ')
        ascii+=1
    if n!=a:
        for k in range(a-n):
            print(k+j, end=' ')
        j=k+j+1
    n-=1
    print()


# n = int(input())
# sch = 65
# snum = 0
# for i in range(n):
#     for j in range(n - i):
#         print(chr(sch), end = ' ')
#         sch += 1
#     for j in range(i):
#         print(snum, end = ' ')
#         snum += 1
#     print()
