import sys
sys.stdin = open("dump_input.txt", "r")

def Dump(N, H):
    n = 0
    while N > n:
        id_max = H.index(max(H))
        id_min = H.index(min(H))
        H[id_max] -= 1
        H[id_min] += 1
        n += 1
    return max(H)-min(H)

for tc in range(10):
    N = int(input())
    H = list(map(int, input().split()))
    print('#%d %d' % (tc+1, Dump(N, H)))