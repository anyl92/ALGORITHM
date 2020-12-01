# 1
import collections


def solution(n, garden):
    answer = 0
    flower_list = collections.deque([])
    for i in range(n):
        for j in range(n):
            if garden[i][j]:
                flower_list.append([i, j])

    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while flower_list:
        for _ in range(len(flower_list)):
            y, x = flower_list.popleft()
            for dy, dx in delta:
                yy, xx = y + dy, x + dx
                if 0 <= yy < n and 0 <= xx < n:
                    if not garden[yy][xx]:
                        garden[yy][xx] = 1
                        flower_list.append([yy, xx])
        answer += 1

    return answer - 1


n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

print("solution 함수의 반환 값은", ret2, "입니다.")


# 2
def solution(K, words):
    answer = 0

    len_list = list(map(len, words))
    cnt = 0
    while len_list:
        cur_len = len_list.pop(0)
        cnt += cur_len
        if cnt > 10:
            answer += 1
            cnt = cur_len + 1
            continue
        cnt += 1

    if cnt > 0:
        answer += 1
    return answer


K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

print("solution 함수의 반환 값은", ret, "입니다.")


# 3
import itertools


def solution(arr, K):
    answer = 99999999
    comb_list = list(itertools.combinations(arr, K))
    for comb in comb_list:
        answer = min(max(comb) - min(comb), answer)
    return answer


arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")


# 4
