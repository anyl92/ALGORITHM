#4871
import sys
sys.stdin = open('route_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    result = 0
    tmp = G
    def find(S, G, L, tmp):
        count = 0
        res = ''
        for i in range(len(L)):
            j = 1
            if tmp != L[i][1]:
                count += 1
            if tmp == L[i][j]:
                j = not j
                tmp = L[i][j]
                if tmp == S:
                    return True
                else:
                    res = find(S, G, L, tmp)
                    if res == None:
                        tmp = G
                        continue
                    return True
            if count == len(L):
                return False

    result = find(S, G, L, tmp)
    print('#%d %d' % (tc, int(result)))

