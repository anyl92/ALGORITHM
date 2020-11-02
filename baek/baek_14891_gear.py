import sys
sys.stdin = open('14891.txt', 'r')

gears = [list(map(int, input())) for _ in range(4)]  # S=1  N=0
int_gears = []
for gear in gears:
    cnt, ans = 7, 0
    while cnt != -1:
        tmp = gear.pop(0)
        if tmp:
            ans += 2 ** cnt
        cnt -= 1
    int_gears.append(ans)


def set_j(i):
    if i % 2 != chk:
        return not dir
    else:
        return dir


def turn(i, x):
    if x:
        int_gears[i] = (int_gears[i] | ((int_gears[i] & 1) << 8)) >> 1
    else:
        int_gears[i] = ((int_gears[i] << 1) | (int_gears[i] >> 7)) & ~(1 << 8)


def spread(i, flag):
    while 0 <= i < 3:
        if not xor_list[i]:
            break

        if flag == 1:
            i += 1

        j = set_j(i)
        turn(i, j)

        if flag == -1:
            i -= 1


K = int(input())
for _ in range(K):
    # 맞물린 곳이 같은 지 먼저 확인
    xor_list = []
    for i in range(3):
        xor_list.append(bool(int_gears[i] & (1 << 5)) ^ bool(int_gears[i + 1] & (1 << 1)))

    num, dir = map(int, input().split())
    if dir == -1:
        dir = 0

    i = num - 1
    chk = i % 2

    turn(i, dir)
    spread(i-1, -1)
    spread(i, 1)

res = 0
for i in range(4):
    if int_gears[i] & (1 << 7) == (1 << 7):
        res += 2 ** i
print(res)