import sys
sys.stdin = open('sectionSum_input.txt', 'r')

def sectionSum(N, H):
    s_H = 0
    t_L = []
    for i in range(0, N[1]):
        s_H += H[i]
    t_L.append(s_H)
    for i in range(N[1], len(H)):
        s_H = s_H - H[i-N[1]] + H[i]
        t_L.append(s_H)
    return max(t_L)-min(t_L)

T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    H = list(map(int, input().split()))
    res = sectionSum(N, H)
    print("#%d %d" % (tc, res))