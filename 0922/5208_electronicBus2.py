import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    L = list(map(int, input().split()))
    lenL = len(L)-1
    L += [0 for _ in range(10)]

    tmpl = []
    cnt = 0
    k = 1
    while k < lenL:
        for i in range(1, L[k]+1):
            tmpl += [L[i+k]]
        tmp = max(tmpl)
        if k + tmp >= lenL:
            cnt += 1
            break
        elif k + tmp < len(L) - 1:
            # if tmp == 0:
            #     cnt = 0
            #     break
            cnt += 1
            k += tmp

    print('#%d %d' % (tc, cnt))