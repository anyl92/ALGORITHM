import sys
sys.stdin = open('4008.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    O = list(map(int, input().split()))
    L = list(map(int, input().split()))

    minn = 100000000001
    maxx = -100000000001


    def solve(k, v):
        global minn, maxx
        if k == N:
            if v > maxx:
                maxx = v
            if v < minn:
                minn = v
        else:
            if O[0]:
                O[0] -= 1
                solve(k+1, v+L[k])
                O[0] += 1
            if O[1]:
                O[1] -= 1
                solve(k+1, v-L[k])
                O[1] += 1
            if O[2]:
                O[2] -= 1
                solve(k+1, v*L[k])
                O[2] += 1
            if O[3]:
                O[3] -= 1
                solve(k+1, int(v/L[k]))
                O[3] += 1


    solve(1, L[0])
    print('#%d %d' % (tc, maxx-minn))