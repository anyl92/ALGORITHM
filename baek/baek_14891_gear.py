import sys
sys.stdin = open('14891.txt', 'r')

gears = [list(map(int, input())) for _ in range(4)]  # S=1  N=0
K = int(input())
L = [list(map(int, input().split())) for _ in range(K)]  # 1=시계
print(gears)
print(K, L)

int_gears = []
for gear in gears:
    cnt, ans = 7, 0
    while cnt != -1:
        tmp = gear.pop(0)
        if tmp:
            ans += 2 ** cnt
        cnt -= 1
    int_gears.append(ans)
print(int_gears, '정숫')
print(list(map(bin, int_gears)))

# 맞물린 곳이 같은 지 먼저 확인
xor_list = []
for i in range(3):
    xor_list.append(bool(int_gears[i] & (1 << 5)) ^ bool(int_gears[i+1] & (1 << 1)))
print(xor_list)

# i = 0
# print(int_gears[i] & (1 << 5))
# print(int_gears[i+1] & (1 << 1))

for num, dir in L:
    i = num - 1
    

#     # if dir == 1:  # 시계
#     i = num - 1
#     while i: # 0까지내려가기
#         i -= 1
#         gears[i]
#
#     for i in range(4):
#         gears[i].
