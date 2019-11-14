import sys
sys.stdin = open('1868.txt', 'r')

def display(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()
    print()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(str, input())) for _ in range(N)]
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # 내천


    def bfs(j, i):
        q = [(j, i)]
        L[i][j] = 0
        vst = [[0 for _ in range(N)] for _ in range(N)]
        vst[i][j] = 1

        while q:
            j, i = q.pop(0)
            zero = []
            mine = 0
            for d in dir:
                jj, ii = j+d[0], i+d[1]
                if 0 <= jj < N and 0 <= ii < N and not vst[ii][jj]:
                    if L[ii][jj] != '*':
                        zero += [(jj, ii)]
                    elif L[ii][jj] == '*':
                        mine += 1
            if not mine:
                L[i][j] = 0
                for jj, ii in zero:
                    L[ii][jj] = 0
                    q.append((jj, ii))
                    vst[ii][jj] = 1
            else:
                L[i][j] = mine
                vst[i][j] = 1


    def find_zero(j, i, k):
        global flag
        if k == i:
            flag = True
            return

        if L[i][j] != '*' and L[i][j + 1] != '*' and L[i][j + 2] != '*':
            find_zero(j, i+1, k)
        else:
            flag = False
            return


    cnt = 0
    for i in range(N-2):
        for j in range(N-2):
            flag = False
            if L[i][j] != '*' and L[i][j + 1] != '*' and L[i][j + 2] != '*':
                find_zero(j, i + 1, i + 3)
                if flag and L[i+1][j+1] == '.':
                    bfs(j+1, i+1)
                    cnt += 1
    print(cnt, 'firstcnt')
    display(L)

    summ =0
    for l in L:
        ''.join(map(str, l)).count('.')
        summ += ''.join(map(str, l)).count('.')
    print(summ, 'summ')
        # print(' '.join(map(str, l)))
    print()



    for i in range(N):
        for j in range(N):
            if L[i][j] == '.':
                bfs(j, i)
                cnt += 1
    display(L)


    print(cnt)