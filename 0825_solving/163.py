import sys
sys.stdin = open('input.txt', 'r')
total = 0
a = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
for i in range(len(a)):
    for j in range(3):
        total += a[i][j]
        print(a[i][j], end=' ')
    print()
print(total)
