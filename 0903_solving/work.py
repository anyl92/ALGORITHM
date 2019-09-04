import sys
sys.stdin = open('input.txt', 'r')

def start(L):
    stp = []
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][0] == L[j][1]:
                break
        else:
            stp.append(L[i][0])
    return list(set(stp))

for tc in range(1):
    V, E = map(int, input().split())
    tmp = list(map(int, input().split()))
    L = [tmp[2*i:2*i+2] for i in range(E)]
    print(V, E, L)

    path = []
    stack = start(L)
    print(stack)

    while stack:
        current = stack.pop()
        trash = []

        for edge in L:
            if edge[1] == current:
                break
        else:
            path.append(current)

            for edge in L:
                if edge[0] == current:
                    stack.append(edge[1])
                    trash.append(edge)

            for t in trash:
                L.remove(t)

    print('#{} {}'.format(tc, ' '.join(list(map(str,path)))))