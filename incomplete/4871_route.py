#4871
import sys
sys.stdin = open('route_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    st = []
    visited = []
    st.append(S)
    visited.append(S)

    def find(L, G, st):
        count = 0
        for i in range(len(L)):
            if L[i][0] == st[-1]:
                if not L[i][1] in visited:
                    st.append(L[i][1])
                    visited.append(L[i][1])
                    find(L, G, st)
                elif L[i][0] == st[-1] and L[i][0] in visited:
                    if st != []:
                        st.pop()
            else:
                count += 1
                if count == len(L):
                    if st != []:
                        st.pop()
            if st == []:
                return 0
            elif st[-1] == G:
                return 1

        else:
            return 0

    res = find(L, G, st)
    print('#%d %d' % (tc, res))

