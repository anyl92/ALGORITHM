inp_num = int(input())
ori_num = inp_num
ori_str = str(ori_num)
cnt = 0

while True:
    cnt += 1
    if ori_num < 10:
        ori_str = '0' + ori_str

    add_num = int(ori_str[0]) + int(ori_str[1])
    if add_num < 10:
        new_str = ori_str[1] + str(add_num)
    else:
        new_str = ori_str[1] + str(add_num)[1]
    new_num = int(new_str)

    if new_num == inp_num:
        print(cnt)
        break

    ori_num = new_num
    ori_str = str(ori_num)