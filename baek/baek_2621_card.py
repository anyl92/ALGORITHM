import sys
sys.stdin = open('2621.txt', 'r')

colors, numbers = [], []
for _ in range(5):
    inp_card = ''.join(input().split())
    colors.append(inp_card[0])
    numbers.append(int(inp_card[1]))

counting_list = [0 for _ in range(10)]
for number in numbers:
    counting_list[number] += 1

score_list = [0 for _ in range(9)]

# 1, 4
if len(set(colors)) == 1:
    score_list[3] = 600 + max(numbers)
    for i in range(1, len(counting_list) - 4):
        if counting_list[i] == 1 and counting_list[i+1] == 1 and counting_list[i+2] == 1 and counting_list[i+3] == 1 and counting_list[i+4] == 1:
            score_list[0] = 900 + max(numbers)
# 2, 3, 6
chk_list = [0, 0]
for i, v in enumerate(counting_list):
    if v == 4:
        score_list[1] = 800 + i
        break
    if v == 3:
        score_list[5] = 400 + i
        tmp1 = i * 10
        chk_list[0] = 1
    if v == 2:
        tmp2 = i
        chk_list[1] = 1
    if chk_list == [1, 1]:
        score_list[2] = 700 + tmp1 + tmp2
# 5
for i in range(1, len(counting_list) - 4):
    if counting_list[i] == 1 and counting_list[i+1] == 1 and counting_list[i+2] == 1 and counting_list[i+3] == 1 and counting_list[i+4] == 1:
        score_list[4] = 500 + max(numbers)
# 7, 8
chk_num = 0
for i, v in enumerate(counting_list):
    if v == 2 and chk_num == 0:
        score_list[7] = 200 + i
        chk_num = i
        continue
    if v == 2:
        score_list[6] = 300 + i*10 + chk_num

score_list[8] = 100 + max(numbers)

print(max(score_list))
