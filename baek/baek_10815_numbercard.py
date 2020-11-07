import sys
sys.stdin = open('10815.txt', 'r')

N = int(input())
NL = sorted(list(map(int, input().split())))
M = int(input())
ML = list(map(int, input().split()))
print(N, NL, M, ML)

len_nl = len(NL)
start = 0
end = len_nl
mid = len_nl // 2

for m in ML:
    if m < NL[mid]:
        end = mid
    elif m > NL[mid]:
        start = mid
    elif m == NL[mid]:
        NL.remove(m)