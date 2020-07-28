import sys
sys.stdin = open('15787.txt', 'r')

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(M)]

train = [0 for _ in range(N+1)]

for i in range(M):
    x, y = L[i][0], L[i][1]
    if x == 1:
        z = L[i][2]
        train[y] = train[y] | (1 << z)
    elif x == 2:
        z = L[i][2]
        train[y] = train[y] & ~(1 << z)
    elif x == 3:
        train[y] = train[y] << 1
        train[y] = train[y] & ((1 << 21) - 1)
    else:
        train[y] = train[y] >> 1
        train[y] = train[y] & ~1

print(len(set(train[1:])))

# order_list = []
# for l in L:
#     order_list += [[x-1 for x in l]]
#
# train = [0 for _ in range(N)]
#
# for order in order_list:
#     num = order[0]
#     section = order[1]
#     cur = format(train[section], 'b')
#     if num == 0:
#         seat = order[2]
#         if cur[-seat] and cur[-seat] == 1:
#             continue
#         train[section] += 2 ** seat
#     elif num == 1:
#         seat = order[2]
#         if cur[-seat] and cur[-seat] == 0:
#             continue
#         train[section] -= 2 ** seat
#     elif num == 2:
#         train[section] = train[section] << 1
#     elif num == 3:
#         train[section] = train[section] >> 1
#
# bin_train = [format(x, 'b') for x in train]
# for i, train in enumerate(bin_train):
#     if len(str(train)) > 20:
#         bin_train[i] = train[-20:]
#
# print(len(set(bin_train)))
