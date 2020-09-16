import sys
sys.stdin = open('17265.txt', 'r')

N = int(input())
L = [list(input().split()) for _ in range(N)]
V = [[0 for _ in range(N)] for _ in range(N)]

OP = ['+', '-', '*']
dir = [[1, 0], [0, 1]]  # 아래, 오른쪽

ans_list = []
cur_OP = -1


def recul(y, x, pre):
    global cur_OP

    for yy, xx in dir:
        yy, xx = y+yy, x+xx

        if 0 <= yy < N and 0 <= xx < N:
            pre_int = pre
            if L[y][x] in OP and V[yy][xx] == 0:
                cur_OP = OP.index(L[y][x])

                next_int = int(L[yy][xx])
                if cur_OP == 0:
                    pre += next_int
                elif cur_OP == 1:
                    pre -= next_int
                else:
                    pre *= next_int

            if yy == N - 1 and xx == N - 1:
                ans_list.append(pre)
                return

            recul(yy, xx, pre)
            pre = pre_int


recul(0, 0, int(L[0][0]))
print(max(ans_list), min(ans_list))


# while s:
#     y, x = s.pop()
#     for yy, xx in dir:
#         yy += y
#         xx += x
#
#         if 0 <= yy < N and 0 <= xx < N:
#             next_char = L[yy][xx]
#
#             if not calc_list[-1] in OP and next_char in OP:
#                 calc_list.append(L[yy][xx])
#             elif calc_list[-1] in OP and not next_char in OP:
#                 calc_list.append(L[yy][xx])
#             else:
#                 s.append([yy, xx])
#                 continue
#
#             print(calc_list, yy, y, xx, x, ans)
#
#             if len(calc_list) == 3:
#                 OP_idx = OP.index(calc_list[1])
#                 if OP_idx == 0:
#                     ans = int(calc_list[0]) + int(calc_list[2])
#                 elif OP_idx == 1:
#                     ans = int(calc_list[0]) - int(calc_list[2])
#                 else:
#                     ans = int(calc_list[0]) * int(calc_list[2])
#                 calc_list = [ans]
#
#             V[yy][xx] = 1
#             s.append([yy, xx])
#     print(s, '스택')