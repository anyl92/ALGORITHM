import sys
sys.stdin = open('card_input.txt', 'r')

def Card(N, H):
    C = [-1] * N
    L = [-1] * N
    M = [-1] * N
    iH = int(H)
    for i in range(N):
        L[i] = iH % 10
        iH //= 10

    for i in range(N):
        C[i] = L.count(L[i])

    max_id = C.index(max(C))
    max_num = L[max_id]

    if C.count(max(C)) != 1:
        for i in range(N):
            M[i] = L[max_id]
            if max(C) == C[i]:
                M[i] = L[i]
        max_num = max(M)

    return max_num, max(C)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = str(input())
    res = Card(N, H)
print('#%d %d %d' % (tc, res[0], res[1]))