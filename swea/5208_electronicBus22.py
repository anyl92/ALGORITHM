import sys
sys.stdin = open('input.txt', 'r')

def DFS(n):
    global cnt, res

    if n >= N:
        if res > cnt:
            res = cnt
        return
    if res < cnt:
        return

    else:
        start = n
        move = L[start]
        for i in range(start+move, start, -1):
            cnt += 1
            DFS(i)
            cnt -= 1

T = int(input())
for tc in range(1, T+1):
    L = list(map(int, input().split()))
    N = L[0]
    res = 999999
    cnt = 0
    DFS(1)
    print('#%d %d' % (tc, res-1))