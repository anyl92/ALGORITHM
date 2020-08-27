import sys
sys.stdin = open('parentheses_input.txt', 'r')

calc = str(input())
for i in range(len(calc)):
    if calc[i] == '-':
        plus = calc[:i]
        minus = calc[i+1:]
        minus = minus.replace('-', '+')
        break
    else:
        plus = calc
        minus = ''

plus_res = sum(map(int, plus.split('+')))
if minus:
    minus_res = sum(map(int, minus.split('+')))
    print(plus_res - minus_res)
else:
    print(plus_res)



# calc = list(input())
# for i in range(len(calc)):
#     if calc[i] == '-':
#         plus = calc[:i]
#         minus = calc[i:]
#         break
#     else:
#         plus = calc
#         minus = []
#
# res = 0
# tmp = '0'
# for p in plus:
#     if p == '+':
#         res += int(tmp)
#         tmp = '0'
#     else:
#         tmp += p
# res += int(tmp)
#
# tmp = '0'
# for m in minus:
#     if m == '+' or m == '-':
#         res -= int(tmp)
#         tmp = '0'
#     else:
#         tmp += m
# res -= int(tmp)
# print(res)