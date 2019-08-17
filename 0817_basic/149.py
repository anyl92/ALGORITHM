import sys
sys.stdin = open('input.txt', 'r')

# ten=list(range(1,11))
# odd=[0]*5
# for i in range(5):
#     for num in ten:
#         if num%2:
#             odd[i] = num
#             num = 0
#         break
# print(odd)

a = int(input())
odd = [1, 3, 5, 7, 9]
n = 0
for i in range(a):
    for j in range(a):
        if n > 4:
            n = 0
        print(odd[n], end=' ')
        n+=1
    print()


# n = int(input())
# x = 1
# for i in range(n):
#     for j in range(n):
#         print(x, end = ' ')
#         x = (x + 2) % 10
#     print()
