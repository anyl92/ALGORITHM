import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    D = {}
    for _ in range(N):
        value, key = input().split()
        if D.get(key):
            D[key].append(value)
        else:
            D[key] = [value]

    answer = 1
    for d in D.keys():
        elem_cnt = 1  # 분류
        for _ in D[d]:
            elem_cnt += 1  # 의상

        answer *= elem_cnt  # (분류+의상) 곱해서 모든 경우의 수
    print(answer - 1)  # 모두 없는 경우 1가지 뺌
