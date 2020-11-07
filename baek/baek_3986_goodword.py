import sys
sys.stdin = open('3986.txt', 'r')

import collections

N = int(input())
ans = 0
for _ in range(N):
    word_list = collections.deque(list(input()))
    # print(word_list)
    stack = collections.deque([])

    while word_list:
        cur = word_list.popleft()
        if stack and stack[-1] == cur:
            stack.pop()
        else:
            stack.append(cur)
    # print(stack)
    if not stack:
        ans += 1
    # print('--------------')
print(ans)