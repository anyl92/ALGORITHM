import sys
sys.stdin = open('17265.txt', 'r')

N = int(input())
L = [list(input().split()) for _ in range(N)]
print(N, L)

OP = ['+', '-', '*']
dir = [[1, 0], [0, 1]]  # 아래, 오른쪽

calc_list = []
ans_list = []
s = [[0, 0]]
pre_char = L[0][0]

while s:
    y, x = s.pop()
    for yy, xx in dir:
        yy += y
        xx += x

        if 0 <= yy < N and 0 <= xx < N:
            post_char = L[yy][xx]
            if post_char in OP:
                calc_list = [pre_char, post_char]
            else:
                calc_list += [post_char]
            s.append([yy, xx])

        if len(calc_list) == 3:
            OP_idx = OP.index(calc_list[1])
            if OP_idx == 0:
                ans = int(pre_char) + int(calc_list[2])
            elif OP_idx == 1:
                ans = int(pre_char) - int(calc_list[2])
            else:
                ans = int(pre_char) * int(calc_list[2])
            # ans_list.append(ans)
            pre_char = ans
            calc_list = []
        print(calc_list, yy, y, xx, x, pre_char)
    print(s)
print(ans_list)