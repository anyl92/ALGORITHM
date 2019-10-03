import sys
sys.stdin = open('parentheses_input.txt', 'r')

calc = list(input())
print(calc)

def calculater():
    res = 0
    i = 0
    tmp = ''
    while i < len(calc):
        if calc[i] == '-' and calc[i] == '+':
            if calc[i] == '+':
                while calc[i] != '-':
                    res = int(tmp)
                    i += 1
            else:

        else:
            tmp += calc[i]
            i += 1

            i += 1
            while calc[i] != '-':
                if calc[i] == '+':
                    calc[i] = '-'
                elif i + 1 < len(calc):
                    i += 1
                else:
                    return calc
        elif i + 1 < len(calc):
            i += 1
        else:
            return calc

calculater()
