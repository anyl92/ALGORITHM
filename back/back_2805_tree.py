import sys
sys.stdin = open('2805.txt', 'r')

N, M = list(map(int, input().split()))
L = list(map(int, input().split()))


def dicision(mid):
    res = 0
    for i in range(N):
        res += max(L[i] - mid, 0)
    if M <= res:
        return True
    return False


def binary_search():
    start = 0
    end = max(L)
    while start <= end:
        mid = (start+end)//2
        if (dicision(mid)):
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search())