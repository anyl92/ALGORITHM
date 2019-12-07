import sys
sys.stdin = open('test.txt', 'r')

def solution(A):
    A = sorted(set(A))

    i = 0
    while i < len(A) and A[i] <= 0:
        A.pop(0)
        i += 1

    i=0
    while i < len(A) and A[i] == i+1:
        i += 1

    return i+1

A = [1, 3, 6, 4, 1, 2]
print(solution(A))