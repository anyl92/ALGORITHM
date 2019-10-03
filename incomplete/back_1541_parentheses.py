import sys
sys.stdin = open('parentheses_input.txt', 'r')

def calculater():
    i = 0
    while i < len(calc):
        if calc[i] == '-':
            i += 1
            while i < len(calc):
                if calc[i] == '+':
                    calc[i] = '-'
                elif i + 1 < len(calc):
                    i += 1
                else:
                    return calc
        i += 1
    return calc

calc = list(input())
print(calc)

res = calculater()
print(res)
print(list(map(int, res.split('+'))))
