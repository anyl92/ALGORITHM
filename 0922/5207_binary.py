import sys
sys.stdin = open('input.txt', 'r')

def binary_search(arr):
    cnt = 0
    for num in B:
        low = 0
        high = len(arr)-1

        flag = 0
        while low <= high:
            mid = (low+high) // 2

            if num >= arr[mid]:
                if num == arr[mid]:
                    cnt += 1
                    break
                low = mid + 1
                if flag == 1:
                    break
                flag = 1
            elif num < arr[mid]:
                high = mid - 1
                if flag == -1:
                    break
                flag = -1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    print('#%d %d' % (tc, binary_search(A)))
