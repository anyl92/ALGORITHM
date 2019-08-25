a = int(input())
c = [[0]*a for _ in range(a)]
for i in range(a):
    c[i][0] = 1
    c[i][i] = 1
for i in range(2, a):
    for j in range(1, a):
        c[i][j] = c[i-1][j] + c[i-1][j-1]
for i in range(a-1, -1, -1):
    for j in range(a):
        if not c[i][j]:
            continue
        else:
            print(c[i][j], end=' ')
    print()
