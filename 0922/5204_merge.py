import sys
sys.stdin = open('input.txt', 'r')

def merge_sort(a):
    mid = len(a)

    if len(a) == 1:
        return a

    l = a[:mid//2]
    r = a[mid//2:]

    l = merge_sort(l)
    r = merge_sort(r)
    return merge(l, r)

def merge(left, right):
    global cnt, L
    i = 0
    j = 0
    arr = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    if left[-1] > right[-1]:
        cnt += 1

    while (i < len(left)):
        arr.append(left[i])
        i += 1

    while (j < len(right)):
        arr.append(right[j])
        j += 1

    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0
    L = merge_sort(L)
    print('#%d %d %d' % (tc, L[N//2], cnt))