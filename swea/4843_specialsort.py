import sys
sys.stdin = open('specialsort.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print('#%d' % (tc), end=' ')
    N = int(input())
    a = list(map(int, input().split()))
    sl = [0] * N
    for i in range(N):
        minindex = i
        for j in range(i+1, len(a)):
            if a[minindex] > a[j]:
                minindex = j
        a[i], a[minindex] = a[minindex], a[i]
    b = [0] * 10
    i=0
    while i < 10:
        print(a.pop(), end=' ')
        i+=1
        print(a.pop(0), end=' ')
        i+=1
    print()