import sys
sys.stdin = open('15922.txt', 'r')

N = int(input())
L = []
for _ in range(N):
    front, back = list(map(int, input().split()))
    L += [[front, 1]] + [[back, 0]]
L = sorted(L)

s = []
ans = 0
for num, io in L:
    if io:  # 여는 괄호
        s.append(num)
    else:  # 닫는 괄호
        tmp = s.pop()

    if not s:
        ans += num - tmp
print(ans)

# i, res = 0, 0
# start = L[0][0]
# while True:
#     if i == len(L)-1:
#         end = L[i][0]
#         res += end - start
#         break
#     elif L[i][1] == -1 and L[i+1][1] == 1:
#         end = L[i][0]
#         res += end - start
#         print(start, end, res)
#         start = L[i+1][0]
#         print(start)
#     i += 1
#
# print(res)