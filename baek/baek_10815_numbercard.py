import sys
sys.stdin = open('10815.txt', 'r')

N = int(input())
NL = sorted(list(map(int, input().split())))
M = int(input())
ML = list(map(int, input().split()))


def binary(s, e, m, num):
    if e == s or e - s == 1:
        if NL[s] == num or NL[e] == num:
            print(1, end=' ')
            return
        else:
            print(0, end=' ')
            return

    if num <= NL[m]:  # 2 < 3
        # e = m
        # m = (s + e) // 2
        # print(NL[s:e], s, e, m)
        binary(s, m, (s+e)//2, num)
    elif num > NL[m]:  # 10 > 3
        # s = m
        # m = (s + e) // 2
        # print(NL[s:e+1])
        binary(m, e, (s+e)//2, num)


len_nl = len(NL)
s, e = 0, len_nl - 1
m = (s + e) // 2
for num in ML:
    binary(s, e, m, num)
