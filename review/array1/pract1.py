data = [7, 4, 2, 0, 0, 6, 0, 7, 0]

arr = [[0] for i in range(9)]
cnt = 0
maxcnt = 0
for i in range(9):
    arr[i] = [1]*data[i] + [0]*(8-data[i])
for y in range(8):
    for x in range(9):
        if arr[x][y] == 0:
            cnt += 1
    if maxcnt < cnt and cnt != 9:
        maxcnt = cnt
    cnt = 0
print(maxcnt)