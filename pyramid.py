star = '*'
space = ' '
squ = int(input('크기를 설정하시오. : '))

if squ % 2 == 0:  # 입력이 짝수일때 10라면

    for t in range(2, squ-1, 2):

        if t == 2:
            margin = int(squ / 2) - 1  # 마진이 4
        elif t % 2 == 0:  # t가 2가아닌 짝수면 4, 6, 8
            margin -= 1
        result = t * star
        print(str(margin * space) + result)

elif squ % 2 == 1:  # 입력이 홀수일때 7라면
    for t in range(1, squ-1, 2):
        if t == 1:  # t가 1이면
            margin = int(squ / 2)  # 마진이 3
        elif t % 2 == 1:  # t가 1이아닌 홀수면 3, 5
            margin -= 1
        result = t * star
        print(str(margin * space) + result)
print(star * squ, end='')
