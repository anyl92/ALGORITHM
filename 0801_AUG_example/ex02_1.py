def calc(equation):
    equ_list=[]
    sub_remove = equation.replace('-', ' -')
    print(sub_remove)
    print(sub_remove.split(' '))
    print(list(map(int, sub_remove)))

    return


print(calc('1+1'))
print(calc('1-1'))
print(calc('123+2-124'))
print(calc('-12+12-7979+9191'))
print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))
