import sys
sys.stdin = open('4013.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(4)]
    L = [list(map(int, input().split())) for _ in range(N)]

    for l in L:  # Lidx 쓰기쉽게 바꿔놓음
        l[0] -= 1
        if l[1] == -1:
            l[1] = 0

    for mag, dir in L:
        i, j = mag, mag
        curl = [mag]
        while i < 3:
            if M[i][2] != M[i+1][-2]:
                curl += [i + 1]
            else:
                break
            i += 1

        while j > 0:
            if M[j][-2] != M[j-1][2]:
                curl += [j - 1]
            else:
                break
            j -= 1

        tmp = dir
        for k in curl:
            dir = tmp
            if mag % 2:  # 홀수고
                if not k % 2:  # 짝수일때
                    dir = not dir
            else:
                if k % 2:
                    dir = not dir

            if dir == 1:  # 시계
                M[k].insert(0, M[k].pop())

            else:  # 반시계
                M[k].append(M[k].pop(0))

    res = 0
    for i in range(4):
        if M[i][0]:  # s극
            res += 2**i

    print('#%d %d' % (tc, res))