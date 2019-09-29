import sys
sys.stdin = open('input.txt', 'r')

a = [list(map(int, input().split())) for _ in range(4)]
rowavg = 0
col0avg = 0
col1avg = 0
totavg = 0
for i in range(4):
    for j in range(2):
        rowavg += a[i][j]
        totavg += a[i][j]
    print(rowavg//2, end=' ')
    rowavg = 0
print()
for i in range(4):
    col0avg += a[i][0]
    col1avg += a[i][1]
print(col0avg//4, col1avg//4)
print(totavg//8)

