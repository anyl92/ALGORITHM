import sys
sys.stdin = open('9095.txt', 'r')


def DP(v):
    if v == 0: return 1
    if v < 0: return 0
    if c[v] != -1: return c[v]
    
    res = 0
    for i in range(1, 4):
        res += DP(v-i)

    return res


T = int(input())
while T:
    n = int(input())
    c = [-1] * (n+1)
    print(DP(n))
    T -= 1
