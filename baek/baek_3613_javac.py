import sys
sys.stdin = open('3613.txt', 'r')


def main():
    inp_list = list(input().replace(' ', ''))
    ord_list = []
    res_list = []
    Err_msg = 'Error!'

    for inp in inp_list:
        ord_list.append(ord(inp))

    if 65 <= ord_list[0] < 96:
        return Err_msg
    if ord_list[-1] == 95:
        return Err_msg

    flag = 0
    err = [0, 0]

    for n in ord_list:
        if 65 <= n < 91:  # 대문자면 _+소문자로
            res_list += '_' + chr(n + 32)
            err[1] = 1
        elif n == 95 and flag:
            return Err_msg
        elif n == 95:  # _면 팝
            flag = 1
            err[0] = 1
        elif flag:  # _를 대문자로
            res_list += chr(n-32)
            flag = 0
        else:
            res_list.append(chr(n))

    if err == [1, 1]:
        return Err_msg

    else:
        ans = ''
        for res in res_list:
            ans += res
        return ans


print(main())