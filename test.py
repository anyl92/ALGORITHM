def power_ser(k, N, arr, t):
    global my_max
    if k == N:
        if t.count(0) == 2:
            a = sum(t) % 10
            if a > my_max:
                my_max = a
    else:
        t[k] = arr[k]
        power_ser(k+1, N, arr, t)
        t[k] = 0
        power_ser(k + 1,  N, arr, t)

people_count = int(input())
card_list = [list(map(int, input().split())) for _ in range(people_count)]
b = 0
my_num = 0
for i in range(people_count):
    my_max = 0
    power_ser(0, len(card_list[i]), card_list[i], [0]*len(card_list[i]))
    if my_max > my_num:
        my_num = my_max
        b = i + 1
    elif my_max == my_num:
        if b < i+1:
            b = i+1
print(b)