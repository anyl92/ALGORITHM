import sys
sys.stdin = open('16564.txt', 'r')

N, K = map(int, sys.stdin.readline().split())
L = sorted([int(sys.stdin.readline()) for _ in range(N)])

cnt = 1
while len(L)>1:
    if L[1] - L[0]:  # 같지않으면
        tmp = L[1] - L[0]

        if K >= tmp * cnt:  # 현재 K로 채우기 가능?
            K -= tmp * cnt
            L.pop(0)
            cnt += 1

        else:
            L[0] += K // cnt
            K -= K // cnt * cnt
            break

    else:  # 같으면
        L.pop(0)
        cnt += 1

if K >= cnt:
    L[0] = L[0] + (K // cnt)
print(L[0])

# for i in range(len(L)-1):
#     if L[i+1] - L[i]:  # 같지않으면
#         tmp = L[i+1] - L[i]
#         NL[i] = 1
#         cnt = sum(NL)
#
#         if K >= tmp * cnt:
#             K -= tmp * cnt
#             n = 0
#             while NL[n]:
#                 L[n] += tmp
#                 n += 1
#         else:
#             n = 0
#             while NL[n]:
#                 L[n] += K // cnt
#                 n += 1
#             K -= K // cnt * cnt
#
#     else:  # 같으면
#         NL[i] = 1
#
# if len(set(L)) == 1 and K >= len(L):
#     L[0] = L[0] + (K // len(L))
# print(L[0])