import sys
sys.stdin = open('14891.txt', 'r')

gears = [list(map(int, input())) for _ in range(4)]  # S=1  N=0
# print(gears)

int_gears = []
for gear in gears:
    cnt, ans = 7, 0
    while cnt != -1:
        tmp = gear.pop(0)
        if tmp:
            ans += 2 ** cnt
        cnt -= 1
    int_gears.append(ans)
# print(int_gears, list(map(bin, int_gears)))

K = int(input())
for _ in range(K):
    # 맞물린 곳이 같은 지 먼저 확인
    xor_list = []
    for i in range(3):
        xor_list.append(bool(int_gears[i] & (1 << 5)) ^ bool(int_gears[i + 1] & (1 << 1)))
    # print(xor_list)

    num, dir = map(int, input().split())
    if dir == -1:
        dir = 0

    i = num - 1
    chk = i % 2

    if dir:
        int_gears[i] = (int_gears[i] | ((int_gears[i] & 1) << 8)) >> 1
    else:
        int_gears[i] = ((int_gears[i] << 1) | (int_gears[i] >> 7)) & ~(1 << 8)
    # print(int_gears, list(map(bin, int_gears)), '자신')

    while i:  # 0까지내려가기
        i -= 1
        if not xor_list[i]:
            break

        if i % 2 != chk:
            j = not dir
        else:
            j = dir

        if j:
            int_gears[i] = (int_gears[i] | ((int_gears[i] & 1) << 8)) >> 1
        else:
            int_gears[i] = ((int_gears[i] << 1) | (int_gears[i] >> 7)) & ~(1 << 8)
    # print(int_gears, list(map(bin, int_gears)), '왼쪽')

    i = num - 1
    while i < 3:  # 3까지올라가기
        if not xor_list[i]:
            break

        i += 1
        if i % 2 != chk:
            j = not dir
        else:
            j = dir

        if j:
            int_gears[i] = (int_gears[i] | ((int_gears[i] & 1) << 8)) >> 1
        else:
            int_gears[i] = ((int_gears[i] << 1) | (int_gears[i] >> 7)) & ~(1 << 8)
    # print(int_gears, list(map(bin, int_gears)), '오른쪽')

# print(int_gears, list(map(bin, int_gears)), '초종')

res = 0
for i in range(4):
    if int_gears[i] & (1 << 7) == (1 << 7):
        res += 2 ** i
print(res)