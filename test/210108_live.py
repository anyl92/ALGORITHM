'''
프로그래밍 언어마다 변수를 표기하기 위한 특정한 표기법을 권장한다.
단어를 밑줄로 구분하는 스네이크표기법과, 단어가 바뀔 때마다 대문자로 시작하는 카멜표기법이 대표적이다. 두가지 표기법으로 변환하는 프로그램을 구현하시오. 
ex) this_is_long_variable_name 이 입력되면,
thisIsLongVariableName 이라고 리턴하고,

thisIsLongVariableName 이 입력되면,
this_is_long_variable_name 이라고 리턴한다.

public String changeConvection(String input){
    String result = "";
'''


# def changeConvection(st):
#     s_list = list(st)
#     r_list = []
#
#     flag = 0
#     for i, s in enumerate(s_list):
#         if s == '_':
#             flag = 1
#             continue
#
#         elif flag:
#             r_list.append(s.upper())
#             flag = 0
#
#         elif 65 < ord(s) < 92:
#             r_list.append('_' + chr(ord(s) + 26))
#
#         else:
#             r_list.append(s)
#
#     res = ''
#     for r in r_list:
#         res += r
#     return res
#
#
# print(changeConvection('this_is_long_variable_name'))


'''
Run-Length Encoding은 문자열에서 같은 값이 연속해서 나타나는 것을 그 개수와 반복되는 값으로 표현하는 방법입니다. 즉, 문자가 반복되면, 반복되는 문자의 갯수로 치환하는 것을 말합니다.
ex) AAAAABBBBBBXQQQPP    5A6BX3Q2P
* 문자가 하나만 올 경우는 1X가 아니라 X 형태로 원문대로 치환됩니다.
 
이 알고리즘의 decoding 함수를 구현하시오. 
runLengthDecoding(“5A6BX3Q2P”)    “AAAAABBBBBBXQQQPP” 
숫자는 int 이하의 값, 문자는 대문자만 입력되며, 입력값에 대한 validation check는 하지 않습니다. 


public String runLengthDecoding(String input) {
    String result = "";
'''

def runLengthDecoding(st):
    num_list = [i for i in range(10)]
    str_list = list(map(str, num_list))
    print(str_list)

    res = ''
    k = 1
    for s in st:
        if s in str_list:
            k = int(s)
        else:
            res += k*s
            k = 1

    return res


print(runLengthDecoding('5A6BX3Q2P'))