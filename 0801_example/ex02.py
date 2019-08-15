# 파일명 및 함수명을 변경하지 마시오.
def calc(equation):
    """
    아래에 코드를 작성하시오.
    equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
    계산된 결과를 정수로 반환합니다.
    """
    equ_list = result = []
    add_equ = equation.replace('+', ' +')
    sub_equ = add_equ.replace('-', ' -')
    # print(add_equ, sub_equ)

    equ_list = sub_equ.split(' ')
    # print(equ_list)

    if '' in equ_list:
        equ_list.remove('')
    # print(equ_list)

    # result = map(int, equ_list)
    result=0
    for i in list(map(int, equ_list)):
        result += i
    return result

# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('1+1'))
    print(calc('1-1'))
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))


"""
-로 짼다
+가 없는 것의 맨앞 인덱스에 -를 넣는다
리스트를 다 더한다
"""