import sys
sys.stdin = open('2621.txt', 'r')

cards = []
[cards.append(''.join(input().split())) for _ in range(5)]
# print(cards)

colors = []
numbers = []
for card in cards:
    colors.append(card[0])
    numbers.append(int(card[1]))
# print(colors, numbers)

counting_list = [0 for _ in range(9)]
for number in numbers:
    counting_list[number-1] += 1
# print(counting_list)

score_list = [0 for _ in range(9)]

# 1
if len(set(colors)) == 1:
    for i in range(len(counting_list)-4):
        if counting_list[i] == 1:
            if counting_list[i+1] == 1 and counting_list[i+2] == 1 and counting_list[i+3] == 1 and counting_list[i+4] == 1:
                score_list[0] = 900 + max(numbers)
# 2
for i, v in enumerate(counting_list):
    if v == 4:
        score_list[1] = 800 + (i+1)
# 3
chk_list = [0, 0]
for i, v in enumerate(counting_list):
    if v == 3:
        tmp1 = (i+1) * 10
        chk_list[0] = 1
    if v == 2:
        tmp2 = i+1
        chk_list[1] = 1
    if chk_list == [1, 1]:
        score_list[2] = 700 + tmp1 + tmp2
# 4
if len(set(colors)) == 1:
    score_list[3] = 600 + max(numbers)
# 5
for i in range(len(counting_list)-4):
    if counting_list[i] == 1:
        if counting_list[i+1] == 1 and counting_list[i+2] == 1 and counting_list[i+3] == 1 and counting_list[i+4] == 1:
            score_list[4] = 500 + max(numbers)
# 6
for i, v in enumerate(counting_list):
    if v == 3:
        score_list[5] = 400 + (i+1)
# 7
chk_num = 0
for i, v in enumerate(counting_list):
    if v == 2 and chk_num == 0:
        chk_num = i+1
        continue
    if v == 2:
        score_list[6] = 300 + (i+1)*10 + chk_num
# 8
for i, v in enumerate(counting_list):
    if v == 2:
        score_list[7] = 200 + (i+1)
# 9
score_list[8] = 100 + max(numbers)

# print(score_list)
print(max(score_list))